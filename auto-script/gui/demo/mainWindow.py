import sys
from datetime import datetime

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QListWidget, QListWidgetItem, \
    QTableWidgetItem
from PySide6.QtCore import QTimer
from ui_MainWindow import Ui_MainWindow
from wyy_click_play import NeteaseClickPlaylist


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 所有播放歌单
        self.allPlaylists = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Set up a timer to simulate real-time data updates
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)  # Update every second
        self.music163 = NeteaseClickPlaylist()
        # 用户名和密码登陆
        self.ui.pushButton_1.clicked.connect(self.handle_button_1_click)
        # 扫码登陆
        self.ui.pushButton_2.clicked.connect(self.handle_button_2_click)
        # 点击歌单 加载歌单信息
        # 连接信号到槽函数
        self.ui.comboBox_1.currentIndexChanged.connect(self.on_combobox_changed)

    def on_combobox_changed(self, index):
        # 获取当前选中的文本
        selected_text = self.ui.comboBox_1.currentText()
        # 获取当前时间
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 更新 QLabel 文本
        self.ui.listWidget.addItem(f"{current_time}您选择了: {selected_text}")

        # 获取当前选中的歌单ID
        playlist_id = selected_text.split('(')[1].split(')')[0]
        song_infos = self.music163.getPlayListSongs(playlist_id, self.allPlaylists[playlist_id][1])
       # 打印歌单歌曲信息
        for song_id in song_infos.keys():
            song_info = song_infos[song_id]
            self.ui.listWidget.addItem(f"{song_info[0]} - {song_info[1]}")


    def handle_button_1_click(self):
        username = self.ui.lineEdit_1.text()
        password = self.ui.lineEdit_2.text()
        self.ui.lineEdit_1.setText(f"Username: {username}")
        self.ui.lineEdit_2.setText(f"Password: {password}")

    def handle_button_2_click(self):
        # push_button_2 扫码登陆触发
        if(self.allPlaylists == None):
            self.allPlaylists = self.music163.getPlayLists()
        all_playlists = self.music163.getPlayLists()
        #  打印所有歌单
        for playlist_id in all_playlists.keys():
            self.ui.comboBox_1.addItem(all_playlists[playlist_id][0]+"("+str(playlist_id)+")")
        # 获取 QListWidget 实例
        self.tableWidget = self.ui.tableWidget  # 假设你的 QListWidget 名为 listWidget

        # 设置列数和列标题
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['歌单ID', '歌单名', '歌曲数量', '播放次数', '歌单属性'])

        # 将获取的歌单信息添加到 QTableWidget 中
        for row, playlist_id in enumerate(all_playlists.keys()):
            playlist_info = all_playlists[playlist_id]
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(playlist_id))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(playlist_info[0]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(playlist_info[1])))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(playlist_info[2])))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(playlist_info[3]))

    def update_data(self):
        # Simulate real-time data update
        data = "18202838208"
        self.ui.lineEdit_1.setText(data)
        self.ui.lineEdit_2.setText("******")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
