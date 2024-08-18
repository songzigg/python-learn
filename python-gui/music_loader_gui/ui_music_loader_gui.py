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
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(928, 651)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 30, 801, 541))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.checkBox_wyy = QCheckBox(self.layoutWidget)
        self.checkBox_wyy.setObjectName(u"checkBox_wyy")
        self.checkBox_wyy.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBox_wyy)

        self.checkBox_kg = QCheckBox(self.layoutWidget)
        self.checkBox_kg.setObjectName(u"checkBox_kg")
        self.checkBox_kg.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBox_kg)

        self.checkBox_kw = QCheckBox(self.layoutWidget)
        self.checkBox_kw.setObjectName(u"checkBox_kw")
        self.checkBox_kw.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBox_kw)

        self.checkBox_mg = QCheckBox(self.layoutWidget)
        self.checkBox_mg.setObjectName(u"checkBox_mg")
        self.checkBox_mg.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBox_mg)

        self.checkBox_qq = QCheckBox(self.layoutWidget)
        self.checkBox_qq.setObjectName(u"checkBox_qq")
        self.checkBox_qq.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBox_qq)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_1 = QLabel(self.layoutWidget)
        self.label_1.setObjectName(u"label_1")

        self.horizontalLayout_2.addWidget(self.label_1)

        self.checkBox_QQ = QCheckBox(self.layoutWidget)
        self.checkBox_QQ.setObjectName(u"checkBox_QQ")
        self.checkBox_QQ.setEnabled(True)
        self.checkBox_QQ.setCheckable(True)
        self.checkBox_QQ.setChecked(False)

        self.horizontalLayout_2.addWidget(self.checkBox_QQ)

        self.checkBox_ximalaya = QCheckBox(self.layoutWidget)
        self.checkBox_ximalaya.setObjectName(u"checkBox_ximalaya")
        self.checkBox_ximalaya.setChecked(False)

        self.horizontalLayout_2.addWidget(self.checkBox_ximalaya)

        self.checkBox_lizhi = QCheckBox(self.layoutWidget)
        self.checkBox_lizhi.setObjectName(u"checkBox_lizhi")
        self.checkBox_lizhi.setChecked(False)

        self.horizontalLayout_2.addWidget(self.checkBox_lizhi)

        self.checkBox_5s = QCheckBox(self.layoutWidget)
        self.checkBox_5s.setObjectName(u"checkBox_5s")
        self.checkBox_5s.setChecked(False)

        self.horizontalLayout_2.addWidget(self.checkBox_5s)

        self.checkBox_yiting = QCheckBox(self.layoutWidget)
        self.checkBox_yiting.setObjectName(u"checkBox_yiting")
        self.checkBox_yiting.setChecked(False)

        self.horizontalLayout_2.addWidget(self.checkBox_yiting)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_5.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.progressBar = QProgressBar(self.layoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_6.addWidget(self.progressBar)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_4.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.tableWidget = QTableWidget(self.layoutWidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSortingEnabled(True)

        self.verticalLayout_2.addWidget(self.tableWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"music loader GUI -- mrsong", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u6e90\u4e00\uff1a", None))
        self.checkBox_wyy.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u6613\u4e91\u97f3\u4e50", None))
        self.checkBox_kg.setText(QCoreApplication.translate("MainWindow", u"\u9177\u72d7\u97f3\u4e50", None))
        self.checkBox_kw.setText(QCoreApplication.translate("MainWindow", u"\u9177\u6211\u97f3\u4e50", None))
        self.checkBox_mg.setText(QCoreApplication.translate("MainWindow", u"\u54aa\u5495\u97f3\u4e50", None))
        self.checkBox_qq.setText(QCoreApplication.translate("MainWindow", u"\u5343\u5343\u97f3\u4e50", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u6e90\u4e8c\uff1a", None))
        self.checkBox_QQ.setText(QCoreApplication.translate("MainWindow", u"QQ\u97f3\u4e50", None))
        self.checkBox_ximalaya.setText(QCoreApplication.translate("MainWindow", u"\u559c\u739b\u62c9\u96c5", None))
        self.checkBox_lizhi.setText(QCoreApplication.translate("MainWindow", u"\u8354\u679d\u97f3\u4e50", None))
        self.checkBox_5s.setText(QCoreApplication.translate("MainWindow", u"5Sing\u97f3\u4e50", None))
        self.checkBox_yiting.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u542c\u97f3\u4e50", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u5173\u952e\u5b57\uff1a", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u516c\u4f17\u53f7\uff1amrsong\u5206\u4eab", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u66f2\u4e0b\u8f7d\u8fdb\u5ea6\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u76ee\u5f55\uff1a", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

