from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QScrollArea, QDialogButtonBox

class TextDisplayDialog(QDialog):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setWindowTitle("歌词")

        # 设置布局
        layout = QVBoxLayout(self)

        # 创建可滚动区域
        scroll_area = QScrollArea(self)
        label = QLabel(text, self)
        label.setWordWrap(True)
        scroll_area.setWidget(label)
        scroll_area.setWidgetResizable(True)

        # 添加滚动区域到布局
        layout.addWidget(scroll_area)

        # 创建按钮并连接到对话框的 accept() 方法
        buttons = QDialogButtonBox(QDialogButtonBox.Ok, self)
        buttons.accepted.connect(self.accept)
        layout.addWidget(buttons)