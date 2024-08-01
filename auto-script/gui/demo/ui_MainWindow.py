# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QTableWidget, QTableWidgetItem, QToolBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1229, 643)
        self.action_1 = QAction(MainWindow)
        self.action_1.setObjectName(u"action_1")
        self.action_1.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(81, 74, 53, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(81, 124, 53, 16))
        self.label_3.setScaledContents(False)
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(620, 190, 531, 381))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(230, 70, 311, 32))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(500, 120, 83, 32))
        self.spinBox_1 = QSpinBox(self.centralwidget)
        self.spinBox_1.setObjectName(u"spinBox_1")
        self.spinBox_1.setGeometry(QRect(430, 120, 36, 31))
        self.spinBox_1.setMinimum(1)
        self.comboBox_1 = QComboBox(self.centralwidget)
        self.comboBox_1.setObjectName(u"comboBox_1")
        self.comboBox_1.setGeometry(QRect(142, 122, 251, 32))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(620, 130, 53, 16))
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(700, 120, 251, 32))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(1040, 120, 83, 32))
        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(980, 120, 36, 31))
        self.spinBox_2.setMinimum(1)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 10, 651, 33))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_1 = QLabel(self.layoutWidget)
        self.label_1.setObjectName(u"label_1")

        self.horizontalLayout.addWidget(self.label_1)

        self.lineEdit_1 = QLineEdit(self.layoutWidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.lineEdit_1)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.pushButton_1 = QPushButton(self.layoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.horizontalLayout.addWidget(self.pushButton_1)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(80, 190, 511, 381))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 160, 61, 20))
        font = QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(870, 160, 61, 20))
        self.label_6.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_1.setText(QCoreApplication.translate("MainWindow", u"\u52a8\u4f5c1", None))
#if QT_CONFIG(tooltip)
        self.action_1.setToolTip(QCoreApplication.translate("MainWindow", u"\u52a8\u4f5c\u63d0\u793a", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u626b\u7801\u767b\u5f55", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u5355\u5217\u8868", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u626b\u7801", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u5355\u5faa\u73af", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u66f2\u5217\u8868", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u66f2\u5faa\u73af", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7\u767b\u5f55", None))
        self.lineEdit_1.setInputMask("")
        self.lineEdit_1.setText("")
        self.lineEdit_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801\u767b\u9646", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u5355\u660e\u7ec6", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u63a7\u5236\u53f0", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

