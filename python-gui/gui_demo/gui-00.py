import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Complex Example")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel("Enter your name:")
        self.layout.addWidget(self.label)

        self.textbox = QLineEdit()
        self.layout.addWidget(self.textbox)

        self.button = QPushButton("Submit")
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.on_click)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

    def on_click(self):
        name = self.textbox.text()
        self.result_label.setText(f"Hello, {name}!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())