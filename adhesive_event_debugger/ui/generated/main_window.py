# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(563, 376)
        self.actionE_xit = QAction(MainWindow)
        self.actionE_xit.setObjectName(u"actionE_xit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.messages_group_box2 = QGroupBox(self.centralwidget)
        self.messages_group_box2.setObjectName(u"messages_group_box2")
        self.verticalLayout_3 = QVBoxLayout(self.messages_group_box2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.messages_group_box = QVBoxLayout()
        self.messages_group_box.setObjectName(u"messages_group_box")

        self.verticalLayout_3.addLayout(self.messages_group_box)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.messages_group_box2)

        self.groupbox = QGroupBox(self.centralwidget)
        self.groupbox.setObjectName(u"groupbox")
        self.verticalLayout_2 = QVBoxLayout(self.groupbox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.running_group_box = QVBoxLayout()
        self.running_group_box.setObjectName(u"running_group_box")

        self.verticalLayout_2.addLayout(self.running_group_box)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.groupbox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 563, 22))
        self.menuE_xit = QMenu(self.menubar)
        self.menuE_xit.setObjectName(u"menuE_xit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuE_xit.menuAction())
        self.menuE_xit.addAction(self.actionE_xit)

        self.retranslateUi(MainWindow)
        self.actionE_xit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Adhesive Event Debugger...", None))
        self.actionE_xit.setText(QCoreApplication.translate("MainWindow", u"E&xit", None))
        self.messages_group_box2.setTitle(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Running", None))
        self.menuE_xit.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
    # retranslateUi

