import sys
from datetime import datetime
import time

from PySide6.QtWidgets import (QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QListWidget, QListWidgetItem, \
    QTableWidgetItem, QAbstractItemView, QFileDialog, QStyle)
from PySide6.QtCore import QStandardPaths, QUrl, QFile, QSaveFile, QDir, QIODevice, Slot
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest, QNetworkAccessManager
from ui_music_loader_gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # 设置窗口名称
        self.setWindowTitle("music163客户端小工具")

        self.ui = Ui_MainWindow()
        # 实例化 Ui_MainWindow 并调用 setupUi 方法，将生成的 UI 组件加载到主窗口对象中。。
        # 生成的 UI 组件是一个 QWidget 对象，可以通过 self.ui.centralwidget 访问。
        self.ui.setupUi(self)
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
        self._open_folder_action.triggered.connect(self.on_open_folder)
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(['序号', '歌手', '歌名', '大小', '时长', '专辑', '来源'])
        self.ui.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background:skyblue;color:black;}")
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

    @Slot()
    def on_open_folder(self):

        dir_path = QFileDialog.getExistingDirectory(
            self, "Open Directory", QDir.homePath(), QFileDialog.ShowDirsOnly
        )

        if dir_path:
            dest_dir = QDir(dir_path)
            self.ui.lineEdit_2.setText(QDir.fromNativeSeparators(dest_dir.path()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
