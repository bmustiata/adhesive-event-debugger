# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'event_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(402, 43)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(203, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.send_button = QPushButton(Form)
        self.send_button.setObjectName(u"send_button")

        self.horizontalLayout.addWidget(self.send_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"QueueName", None))
        self.send_button.setText(QCoreApplication.translate("Form", u"Send", None))
    # retranslateUi

