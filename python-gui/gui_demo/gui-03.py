import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction, QApplication, QLabel, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()
        # 表示该小部件使用自定义的上下文菜单策略。这意味着上下文菜单不会自动显示，而是需要手动处理。
        # 通过 customContextMenuRequested 信号处理。
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()