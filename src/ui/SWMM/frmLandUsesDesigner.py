# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dev\Python\dev-ui\src\ui\SWMM\frmLandUsesDesigner.ui'
#
# Created by: PyQt5 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_frmLandUsesEditor(object):
    def setupUi(self, frmLandUsesEditor):
        frmLandUsesEditor.setObjectName(_fromUtf8("frmLandUsesEditor"))
        frmLandUsesEditor.resize(401, 383)
        font = QFont()
        font.setPointSize(10)
        frmLandUsesEditor.setFont(font)
        self.centralWidget = QWidget(frmLandUsesEditor)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_3 = QVBoxLayout(self.centralWidget)
        # self.verticalLayout_3.setMargin(11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabLanduse = QTabWidget(self.centralWidget)
        self.tabLanduse.setObjectName(_fromUtf8("tabLanduse"))
        self.General = QWidget()
        self.General.setObjectName(_fromUtf8("General"))
        self.verticalLayout_2 = QVBoxLayout(self.General)
        # self.verticalLayout_2.setMargin(11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.fraGeneral = QFrame(self.General)
        self.fraGeneral.setFrameShape(QFrame.StyledPanel)
        self.fraGeneral.setFrameShadow(QFrame.Raised)
        self.fraGeneral.setObjectName(_fromUtf8("fraGeneral"))
        self.horizontalLayout_2 = QHBoxLayout(self.fraGeneral)
        # self.horizontalLayout_2.setMargin(11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tblGeneral = QTableWidget(self.fraGeneral)
        self.tblGeneral.setObjectName(_fromUtf8("tblGeneral"))
        self.tblGeneral.setColumnCount(1)
        self.tblGeneral.setRowCount(0)
        item = QTableWidgetItem()
        self.tblGeneral.setHorizontalHeaderItem(0, item)
        self.horizontalLayout_2.addWidget(self.tblGeneral)
        self.verticalLayout_2.addWidget(self.fraGeneral)
        self.fraNotesGeneral = QFrame(self.General)
        self.fraNotesGeneral.setFrameShape(QFrame.StyledPanel)
        self.fraNotesGeneral.setFrameShadow(QFrame.Raised)
        self.fraNotesGeneral.setObjectName(_fromUtf8("fraNotesGeneral"))
        self.verticalLayout = QVBoxLayout(self.fraNotesGeneral)
        # self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblNotesGeneral = QLabel(self.fraNotesGeneral)
        self.lblNotesGeneral.setWordWrap(True)
        self.lblNotesGeneral.setObjectName(_fromUtf8("lblNotesGeneral"))
        self.verticalLayout.addWidget(self.lblNotesGeneral)
        self.verticalLayout_2.addWidget(self.fraNotesGeneral)
        self.tabLanduse.addTab(self.General, _fromUtf8(""))
        self.Buildup = QWidget()
        self.Buildup.setObjectName(_fromUtf8("Buildup"))
        self.verticalLayout_6 = QVBoxLayout(self.Buildup)
        # self.verticalLayout_6.setMargin(11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.fraBuildup = QFrame(self.Buildup)
        self.fraBuildup.setFrameShape(QFrame.StyledPanel)
        self.fraBuildup.setFrameShadow(QFrame.Raised)
        self.fraBuildup.setObjectName(_fromUtf8("fraBuildup"))
        self.horizontalLayout_3 = QHBoxLayout(self.fraBuildup)
        # self.horizontalLayout_3.setMargin(11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tblBuildup = QTableWidget(self.fraBuildup)
        self.tblBuildup.setObjectName(_fromUtf8("tblBuildup"))
        self.tblBuildup.setColumnCount(1)
        self.tblBuildup.setRowCount(0)
        item = QTableWidgetItem()
        self.tblBuildup.setHorizontalHeaderItem(0, item)
        self.horizontalLayout_3.addWidget(self.tblBuildup)
        self.verticalLayout_6.addWidget(self.fraBuildup)
        self.fraNotesBuildup = QFrame(self.Buildup)
        self.fraNotesBuildup.setFrameShape(QFrame.StyledPanel)
        self.fraNotesBuildup.setFrameShadow(QFrame.Raised)
        self.fraNotesBuildup.setObjectName(_fromUtf8("fraNotesBuildup"))
        self.verticalLayout_4 = QVBoxLayout(self.fraNotesBuildup)
        # self.verticalLayout_4.setMargin(11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lblNotesBuildup = QLabel(self.fraNotesBuildup)
        self.lblNotesBuildup.setWordWrap(True)
        self.lblNotesBuildup.setObjectName(_fromUtf8("lblNotesBuildup"))
        self.verticalLayout_4.addWidget(self.lblNotesBuildup)
        self.verticalLayout_6.addWidget(self.fraNotesBuildup)
        self.tabLanduse.addTab(self.Buildup, _fromUtf8(""))
        self.Washoff = QWidget()
        self.Washoff.setObjectName(_fromUtf8("Washoff"))
        self.verticalLayout_7 = QVBoxLayout(self.Washoff)
        # self.verticalLayout_7.setMargin(11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.fraWashoff = QFrame(self.Washoff)
        self.fraWashoff.setFrameShape(QFrame.StyledPanel)
        self.fraWashoff.setFrameShadow(QFrame.Raised)
        self.fraWashoff.setObjectName(_fromUtf8("fraWashoff"))
        self.horizontalLayout_4 = QHBoxLayout(self.fraWashoff)
        # self.horizontalLayout_4.setMargin(11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.tblWashoff = QTableWidget(self.fraWashoff)
        self.tblWashoff.setObjectName(_fromUtf8("tblWashoff"))
        self.tblWashoff.setColumnCount(1)
        self.tblWashoff.setRowCount(0)
        item = QTableWidgetItem()
        self.tblWashoff.setHorizontalHeaderItem(0, item)
        self.horizontalLayout_4.addWidget(self.tblWashoff)
        self.verticalLayout_7.addWidget(self.fraWashoff)
        self.fraNotesWashoff = QFrame(self.Washoff)
        self.fraNotesWashoff.setFrameShape(QFrame.StyledPanel)
        self.fraNotesWashoff.setFrameShadow(QFrame.Raised)
        self.fraNotesWashoff.setObjectName(_fromUtf8("fraNotesWashoff"))
        self.verticalLayout_5 = QVBoxLayout(self.fraNotesWashoff)
        # self.verticalLayout_5.setMargin(11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lblNotesWashoff = QLabel(self.fraNotesWashoff)
        self.lblNotesWashoff.setWordWrap(True)
        self.lblNotesWashoff.setObjectName(_fromUtf8("lblNotesWashoff"))
        self.verticalLayout_5.addWidget(self.lblNotesWashoff)
        self.verticalLayout_7.addWidget(self.fraNotesWashoff)
        self.tabLanduse.addTab(self.Washoff, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabLanduse)
        self.fraOKCancel = QFrame(self.centralWidget)
        self.fraOKCancel.setFrameShape(QFrame.StyledPanel)
        self.fraOKCancel.setFrameShadow(QFrame.Raised)
        self.fraOKCancel.setObjectName(_fromUtf8("fraOKCancel"))
        self.horizontalLayout = QHBoxLayout(self.fraOKCancel)
        # self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QSpacerItem(338, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cmdOK = QPushButton(self.fraOKCancel)
        self.cmdOK.setObjectName(_fromUtf8("cmdOK"))
        self.horizontalLayout.addWidget(self.cmdOK)
        self.cmdCancel = QPushButton(self.fraOKCancel)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.verticalLayout_3.addWidget(self.fraOKCancel)
        frmLandUsesEditor.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmLandUsesEditor)
        self.tabLanduse.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmLandUsesEditor)

    def retranslateUi(self, frmLandUsesEditor):
        frmLandUsesEditor.setWindowTitle(_translate("frmLandUsesEditor", "SWMM Land Use Editor", None))
        item = self.tblGeneral.horizontalHeaderItem(0)
        item.setText(_translate("frmLandUsesEditor", "Value", None))
        self.lblNotesGeneral.setText(_translate("frmLandUsesEditor", "Explanatory notes", None))
        self.tabLanduse.setTabText(self.tabLanduse.indexOf(self.General), _translate("frmLandUsesEditor", "General", None))
        item = self.tblBuildup.horizontalHeaderItem(0)
        item.setText(_translate("frmLandUsesEditor", "Value", None))
        self.lblNotesBuildup.setText(_translate("frmLandUsesEditor", "Explanatory notes", None))
        self.tabLanduse.setTabText(self.tabLanduse.indexOf(self.Buildup), _translate("frmLandUsesEditor", "Buildup", None))
        item = self.tblWashoff.horizontalHeaderItem(0)
        item.setText(_translate("frmLandUsesEditor", "Value", None))
        self.lblNotesWashoff.setText(_translate("frmLandUsesEditor", "Explanatory notes", None))
        self.tabLanduse.setTabText(self.tabLanduse.indexOf(self.Washoff), _translate("frmLandUsesEditor", "Washoff", None))
        self.cmdOK.setText(_translate("frmLandUsesEditor", "OK", None))
        self.cmdCancel.setText(_translate("frmLandUsesEditor", "Cancel", None))

