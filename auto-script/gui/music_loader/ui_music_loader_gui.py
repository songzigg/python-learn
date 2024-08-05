# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'music_loader_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(822, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 30, 721, 441))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.checkBox_wyy = QCheckBox(self.widget)
        self.checkBox_wyy.setObjectName(u"checkBox_wyy")

        self.horizontalLayout.addWidget(self.checkBox_wyy)

        self.checkBox_kg = QCheckBox(self.widget)
        self.checkBox_kg.setObjectName(u"checkBox_kg")

        self.horizontalLayout.addWidget(self.checkBox_kg)

        self.checkBox_QQ = QCheckBox(self.widget)
        self.checkBox_QQ.setObjectName(u"checkBox_QQ")

        self.horizontalLayout.addWidget(self.checkBox_QQ)

        self.checkBox_kw = QCheckBox(self.widget)
        self.checkBox_kw.setObjectName(u"checkBox_kw")

        self.horizontalLayout.addWidget(self.checkBox_kw)

        self.checkBox_mg = QCheckBox(self.widget)
        self.checkBox_mg.setObjectName(u"checkBox_mg")

        self.horizontalLayout.addWidget(self.checkBox_mg)

        self.checkBox_qq = QCheckBox(self.widget)
        self.checkBox_qq.setObjectName(u"checkBox_qq")

        self.horizontalLayout.addWidget(self.checkBox_qq)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_3.addWidget(self.progressBar)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.tableWidget = QTableWidget(self.widget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSortingEnabled(True)

        self.verticalLayout_2.addWidget(self.tableWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 822, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u6e90\uff1a", None))
        self.checkBox_wyy.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u6613\u4e91\u97f3\u4e50", None))
        self.checkBox_kg.setText(QCoreApplication.translate("MainWindow", u"\u9177\u72d7\u97f3\u4e50", None))
        self.checkBox_QQ.setText(QCoreApplication.translate("MainWindow", u"QQ\u97f3\u4e50", None))
        self.checkBox_kw.setText(QCoreApplication.translate("MainWindow", u"\u9177\u6211\u97f3\u4e50", None))
        self.checkBox_mg.setText(QCoreApplication.translate("MainWindow", u"\u54aa\u5495\u97f3\u4e50", None))
        self.checkBox_qq.setText(QCoreApplication.translate("MainWindow", u"\u5343\u5343\u97f3\u4e50", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u5173\u952e\u5b57\uff1a", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8001\u8fa3\u6912\u7684techHub", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u66f2\u4e0b\u8f7d\u8fdb\u5ea6\uff1a", None))
    # retranslateUi

