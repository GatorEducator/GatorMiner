# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newtab.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewTab(object):
    def setupUi(self, NewTab):
        NewTab.setObjectName("NewTab")
        NewTab.resize(400, 85)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(NewTab)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewTab)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox, 0, QtCore.Qt.AlignBottom)

        self.retranslateUi(NewTab)
        self.buttonBox.accepted.connect(NewTab.accept)
        self.buttonBox.rejected.connect(NewTab.reject)
        QtCore.QMetaObject.connectSlotsByName(NewTab)

    def retranslateUi(self, NewTab):
        _translate = QtCore.QCoreApplication.translate
        NewTab.setWindowTitle(_translate("NewTab", "Dialog"))
