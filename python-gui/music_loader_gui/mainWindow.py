import sys
import os
from datetime import datetime
import time

import requests
from PySide6 import QtCore
from PySide6.QtWidgets import (QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QListWidget, QListWidgetItem, \
                               QTableWidgetItem, QAbstractItemView, QFileDialog, QStyle, QMenu, QProgressBar, QLabel,
                               QMessageBox)
from PySide6.QtCore import QStandardPaths, QUrl, QFile, QSaveFile, QDir, QIODevice, Slot
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest, QNetworkAccessManager
from ui_music_loader_gui import Ui_MainWindow
from musicdl import musicdl
from modules.utils import Downloader, touchdir
from PySide6.QtGui import QIcon, Qt, QCursor
from TextDisplayDilog import TextDisplayDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 初始化
        config = {'logfilepath': 'musicdl.log', 'savedir': 'downloaded', 'search_size_per_source': 2, 'proxies': {}}
        self.music_api = musicdl(config=config)
        # 设置窗口名称
        self.setWindowTitle("mrsong分享 -- 音乐下载客户端")
        self.ui = Ui_MainWindow()
        # 实例化 Ui_MainWindow 并调用 setupUi 方法，将生成的 UI 组件加载到主窗口对象中。。
        # 生成的 UI 组件是一个 QWidget 对象，可以通过 self.ui.centralwidget 访问。
        self.ui.setupUi(self)
        # 设置窗口图标
        self.setWindowIcon(QIcon(os.path.join(os.path.dirname(__file__), 'icon.ico')))
        self.setFixedSize(840, 480)
        self.initialize()
        # Open folder action
        self._open_folder_action = self.ui.lineEdit_2.addAction(
            qApp.style().standardIcon(QStyle.StandardPixmap.SP_DirOpenIcon),  # noqa: F821
            QLineEdit.TrailingPosition
        )
        self.ui.lineEdit_2.setText(
            QDir.fromNativeSeparators(
                QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)
            )
        )
        self.dest_dir = QDir(QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)).path()
        self._open_folder_action.triggered.connect(self.on_open_folder)
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(['序号', '歌手', '歌名', '大小', '时长', '专辑', '来源'])
        self.ui.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;color:black;}")
        # 设置表格不可编辑
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置表格选择行为为选择整行
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 鼠标右键点击的菜单
        self.context_menu = QMenu(self)
        self.action_download = self.context_menu.addAction('下载')
        self.lyric_show = self.context_menu.addAction('歌词')
        # 进度条
        self.bar_download = QProgressBar(self)
        self.label_download = QLabel('歌曲下载进度:')
        # 绑定事件
        self.ui.pushButton.clicked.connect(self.search)
        self.ui.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.tableWidget.customContextMenuRequested.connect(self.mouseclick)
        #  table 数据可滑动
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 确保滚动条始终可见
        self.ui.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.ui.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.action_download.triggered.connect(self.download)
        self.lyric_show.triggered.connect(self.showLyric)

    # 初始化 搜索结果 和 音乐记录 和选择的音乐索引
    def initialize(self):
        self.search_results = {}
        self.music_records = {}
        self.selected_music_idx = -10000

    '''鼠标右键点击事件'''
    @Slot()
    def mouseclick(self):
        # 将上下文菜单移动到当前鼠标的位置。这样当你右键点击时，上下文菜单就会在你点击的位置弹出。
        self.context_menu.move(QCursor().pos())
        self.context_menu.show()
    @Slot()
    def search(self):
        self.initialize()
        target_srcs_dict = {
            'QQ音乐': 'qqmusic',
            '酷我音乐': 'kuwo',
            '咪咕音乐': 'migu',
            '千千音乐': 'qianqian',
            '酷狗音乐': 'kugou',
            '网易云音乐': 'netease',
            '一听音乐': 'yiting',
            '喜马拉雅': 'ximalaya',
            '荔枝音乐': 'lizhi',
            '5Sing音乐': 'fivesing'
        }
        selected_src_names = []
        if self.ui.checkBox_wyy.isChecked():
            selected_src_names.append('网易云音乐')
        if self.ui.checkBox_kg.isChecked():
            selected_src_names.append('酷狗音乐')
        if self.ui.checkBox_QQ.isChecked():
            selected_src_names.append('QQ音乐')
        if self.ui.checkBox_kw.isChecked():
            selected_src_names.append('酷我音乐')
        if self.ui.checkBox_mg.isChecked():
            selected_src_names.append('咪咕音乐')
        if self.ui.checkBox_qq.isChecked():
            selected_src_names.append('千千音乐')
        if self.ui.checkBox_yiting.isChecked():
            selected_src_names.append('一听音乐')
        if self.ui.checkBox_ximalaya.isChecked():
            selected_src_names.append('喜马拉雅')
        if self.ui.checkBox_lizhi.isChecked():
            selected_src_names.append('荔枝音乐')
        if self.ui.checkBox_5s.isChecked():
            selected_src_names.append('5Sing音乐')
        target_srcs = [target_srcs_dict.get(name) for name in selected_src_names]
        keyword = self.ui.lineEdit.text()
        self.search_results = self.music_api.search(keyword, target_srcs)
        count, row = 0, 0
        # 设置表格行数
        for value in self.search_results.values():
            count += len(value)
        self.ui.tableWidget.setRowCount(count)
        # 设置表格内容
        for _, (key, values) in enumerate(self.search_results.items()):
            for _, value in enumerate(values):
                for column, item in enumerate([str(row), value['singers'], value['songname'], value['filesize'], value['duration'], value['album'], value['source']]):
                    self.ui.tableWidget.setItem(row, column, QTableWidgetItem(item))
                    self.ui.tableWidget.item(row, column).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.music_records.update({str(row): value})
                row += 1
        return self.search_results


    '''下载'''
    @Slot()
    def download(self):
        self.selected_music_idx = str(self.ui.tableWidget.selectedItems()[0].row())
        songinfo = self.music_records.get(self.selected_music_idx)
        headers = Downloader(songinfo).headers
        songinfo['savedir'] = self.dest_dir
        # touchdir(songinfo['savedir'])
        # 检查 'savedir' 是否存在，如果不存在则创建
        if not os.path.exists(songinfo['savedir']):
            os.makedirs(songinfo['savedir'])
        try:
            with requests.get(songinfo['download_url'], headers=headers, stream=True, verify=False) as response:
                if response.status_code == 200:
                    total_size, chunk_size, download_size = int(response.headers['content-length']), 1024, 0
                    with open(os.path.join(songinfo['savedir'], songinfo['savename'] + '.' + songinfo['ext']),
                              'wb') as fp:
                        for chunk in response.iter_content(chunk_size=chunk_size):
                            if chunk:
                                fp.write(chunk)
                                download_size += len(chunk)
                                self.bar_download.setValue(int(download_size / total_size * 100))
                   # 下载歌词到文本中 歌词在songs[lyric] 中
                   #  with open(os.path.join(songinfo['savedir'], songinfo['savename'] + '_lyric.txt'), 'w') as f:
                   #      f.write(songinfo['lyric'])

            QMessageBox().information(self, '下载完成', '歌曲%s已经下载完成, 保存在当前路径的%s文件夹下' % (
            songinfo['savename'], songinfo['savedir']))
            self.bar_download.setValue(0)
        except PermissionError:
             print(f"Error: No permission to write in the directory {songinfo['savedir']}")

    @Slot()
    def showLyric(self):
        self.selected_music_idx = str(self.ui.tableWidget.selectedItems()[0].row())
        songinfo = self.music_records.get(self.selected_music_idx)
        # 创建并显示对话框
        dialog = TextDisplayDialog(songinfo['lyric'])
        dialog.exec()

    @Slot()
    def on_open_folder(self):

        # 打开文件夹
        dir_path = QFileDialog.getExistingDirectory(
            self, "Open Directory", QDir.homePath(), QFileDialog.ShowDirsOnly
        )

        # 如果用户选择了文件夹
        if dir_path:
            dest_dir = QDir(dir_path)
            self.ui.lineEdit_2.setText(QDir.fromNativeSeparators(dest_dir.path()))
            self.dest_dir = dest_dir.path()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
