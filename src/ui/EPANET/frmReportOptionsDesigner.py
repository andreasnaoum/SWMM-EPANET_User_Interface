# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dev\Python\dev-ui\src\ui\EPANET\frmReportOptionsDesigner.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_frmReportOptions(object):
    def setupUi(self, frmReportOptions):
        frmReportOptions.setObjectName(_fromUtf8("frmReportOptions"))
        frmReportOptions.resize(386, 689)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmReportOptions.setFont(font)
        self.centralWidget = QtGui.QWidget(frmReportOptions)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.fraTop = QtGui.QFrame(self.centralWidget)
        self.fraTop.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraTop.setFrameShadow(QtGui.QFrame.Raised)
        self.fraTop.setObjectName(_fromUtf8("fraTop"))
        self.gridLayout = QtGui.QGridLayout(self.fraTop)
        self.gridLayout.setMargin(11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblPageSize = QtGui.QLabel(self.fraTop)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPageSize.setFont(font)
        self.lblPageSize.setObjectName(_fromUtf8("lblPageSize"))
        self.gridLayout.addWidget(self.lblPageSize, 0, 0, 1, 1)
        self.txtPageSize = QtGui.QLineEdit(self.fraTop)
        self.txtPageSize.setObjectName(_fromUtf8("txtPageSize"))
        self.gridLayout.addWidget(self.txtPageSize, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(110, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.lblReportFileName = QtGui.QLabel(self.fraTop)
        self.lblReportFileName.setObjectName(_fromUtf8("lblReportFileName"))
        self.gridLayout.addWidget(self.lblReportFileName, 1, 0, 1, 1)
        self.txtReportFileName = QtGui.QLineEdit(self.fraTop)
        self.txtReportFileName.setObjectName(_fromUtf8("txtReportFileName"))
        self.gridLayout.addWidget(self.txtReportFileName, 1, 1, 1, 2)
        self.lblStatus = QtGui.QLabel(self.fraTop)
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
        self.gridLayout.addWidget(self.lblStatus, 2, 0, 1, 1)
        self.cboStatus = QtGui.QComboBox(self.fraTop)
        self.cboStatus.setObjectName(_fromUtf8("cboStatus"))
        self.gridLayout.addWidget(self.cboStatus, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(110, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.lblSummary = QtGui.QLabel(self.fraTop)
        self.lblSummary.setObjectName(_fromUtf8("lblSummary"))
        self.gridLayout.addWidget(self.lblSummary, 3, 0, 1, 1)
        self.cboSummary = QtGui.QComboBox(self.fraTop)
        self.cboSummary.setObjectName(_fromUtf8("cboSummary"))
        self.gridLayout.addWidget(self.cboSummary, 3, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(110, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)
        self.lblEnergy = QtGui.QLabel(self.fraTop)
        self.lblEnergy.setObjectName(_fromUtf8("lblEnergy"))
        self.gridLayout.addWidget(self.lblEnergy, 4, 0, 1, 1)
        self.cboEnergy = QtGui.QComboBox(self.fraTop)
        self.cboEnergy.setObjectName(_fromUtf8("cboEnergy"))
        self.gridLayout.addWidget(self.cboEnergy, 4, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(110, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 2, 1, 1)
        self.verticalLayout.addWidget(self.fraTop)
        self.gbxNode = QtGui.QGroupBox(self.centralWidget)
        self.gbxNode.setObjectName(_fromUtf8("gbxNode"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gbxNode)
        self.gridLayout_2.setMargin(11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lblLimit = QtGui.QLabel(self.gbxNode)
        self.lblLimit.setObjectName(_fromUtf8("lblLimit"))
        self.gridLayout_2.addWidget(self.lblLimit, 0, 1, 1, 1)
        self.lblPrecision = QtGui.QLabel(self.gbxNode)
        self.lblPrecision.setObjectName(_fromUtf8("lblPrecision"))
        self.gridLayout_2.addWidget(self.lblPrecision, 0, 3, 1, 1)
        self.cbxNode1 = QtGui.QCheckBox(self.gbxNode)
        self.cbxNode1.setObjectName(_fromUtf8("cbxNode1"))
        self.gridLayout_2.addWidget(self.cbxNode1, 1, 0, 1, 1)
        self.cboNode1 = QtGui.QComboBox(self.gbxNode)
        self.cboNode1.setObjectName(_fromUtf8("cboNode1"))
        self.gridLayout_2.addWidget(self.cboNode1, 1, 1, 1, 1)
        self.txtNode1 = QtGui.QLineEdit(self.gbxNode)
        self.txtNode1.setObjectName(_fromUtf8("txtNode1"))
        self.gridLayout_2.addWidget(self.txtNode1, 1, 2, 1, 1)
        self.txtNode6 = QtGui.QLineEdit(self.gbxNode)
        self.txtNode6.setObjectName(_fromUtf8("txtNode6"))
        self.gridLayout_2.addWidget(self.txtNode6, 1, 3, 1, 1)
        self.cbxNode2 = QtGui.QCheckBox(self.gbxNode)
        self.cbxNode2.setObjectName(_fromUtf8("cbxNode2"))
        self.gridLayout_2.addWidget(self.cbxNode2, 2, 0, 1, 1)
        self.cboNode2 = QtGui.QComboBox(self.gbxNode)
        self.cboNode2.setObjectName(_fromUtf8("cboNode2"))
        self.gridLayout_2.addWidget(self.cboNode2, 2, 1, 1, 1)
        self.txtNode2 = QtGui.QLineEdit(self.gbxNode)
        self.txtNode2.setObjectName(_fromUtf8("txtNode2"))
        self.gridLayout_2.addWidget(self.txtNode2, 2, 2, 1, 1)
        self.txtNode7 = QtGui.QLineEdit(self.gbxNode)
        self.txtNode7.setObjectName(_fromUtf8("txtNode7"))
        self.gridLayout_2.addWidget(self.txtNode7, 2, 3, 1, 1)
        self.cbxNode3 = QtGui.QCheckBox(self.gbxNode)
        self.cbxNode3.setObjectName(_fromUtf8("cbxNode3"))
        self.gridLayout_2.addWidget(self.cbxNode3, 3, 0, 1, 1)
        self.cboNode3 = QtGui.QComboBox(self.gbxNode)
        self.cboNode3.setObjectName(_fromUtf8("cboNode3"))
        self.gridLayout_2.addWidget(self.cboNode3, 3, 1, 1, 1)
        self.txtNode3 = QtGui.QLineEdit(self.gbxNode)
        self.txtNode3.setObjectName(_fromUtf8("txtNode3"))
        self.gridLayout_2.addWidget(self.txtNode3, 3, 2, 1, 1)
        self.txtNode8 = QtGui.QLineEdit(self.gbxNode)
        self.txtNode8.setObjectName(_fromUtf8("txtNode8"))
        self.gridLayout_2.addWidget(self.txtNode8, 3, 3, 1, 1)
        self.cbxNode4 = QtGui.QCheckBox(self.gbxNode)
        self.cbxNode4.setObjectName(_fromUtf8("cbxNode4"))
        self.gridLayout_2.addWidget(self.cbxNode4, 4, 0, 1, 1)
        self.cboNode4 = QtGui.QComboBox(self.gbxNode)
        self.cboNode4.setObjectName(_fromUtf8("cboNode4"))
        self.gridLayout_2.addWidget(self.cboNode4, 4, 1, 1, 1)
        self.txtNode4 = QtGui.QLineEdit(self.gbxNode)
        self.txtNode4.setObjectName(_fromUtf8("txtNode4"))
        self.gridLayout_2.addWidget(self.txtNode4, 4, 2, 1, 1)
        self.txtNode9 = QtGui.QLineEdit(self.gbxNode)
        self.txtNode9.setObjectName(_fromUtf8("txtNode9"))
        self.gridLayout_2.addWidget(self.txtNode9, 4, 3, 1, 1)
        self.cbxNode5 = QtGui.QCheckBox(self.gbxNode)
        self.cbxNode5.setObjectName(_fromUtf8("cbxNode5"))
        self.gridLayout_2.addWidget(self.cbxNode5, 5, 0, 1, 1)
        self.cboNode5 = QtGui.QComboBox(self.gbxNode)
        self.cboNode5.setObjectName(_fromUtf8("cboNode5"))
        self.gridLayout_2.addWidget(self.cboNode5, 5, 1, 1, 1)
        self.txtNode5 = QtGui.QLineEdit(self.gbxNode)
        self.txtNode5.setObjectName(_fromUtf8("txtNode5"))
        self.gridLayout_2.addWidget(self.txtNode5, 5, 2, 1, 1)
        self.txtNode10 = QtGui.QLineEdit(self.gbxNode)
        self.txtNode10.setObjectName(_fromUtf8("txtNode10"))
        self.gridLayout_2.addWidget(self.txtNode10, 5, 3, 1, 1)
        self.verticalLayout.addWidget(self.gbxNode)
        self.gbxLink = QtGui.QGroupBox(self.centralWidget)
        self.gbxLink.setObjectName(_fromUtf8("gbxLink"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gbxLink)
        self.gridLayout_3.setMargin(11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lblLimitLink = QtGui.QLabel(self.gbxLink)
        self.lblLimitLink.setObjectName(_fromUtf8("lblLimitLink"))
        self.gridLayout_3.addWidget(self.lblLimitLink, 0, 1, 1, 1)
        self.lblPrecisionLink = QtGui.QLabel(self.gbxLink)
        self.lblPrecisionLink.setObjectName(_fromUtf8("lblPrecisionLink"))
        self.gridLayout_3.addWidget(self.lblPrecisionLink, 0, 3, 1, 1)
        self.cbxLink1 = QtGui.QCheckBox(self.gbxLink)
        self.cbxLink1.setObjectName(_fromUtf8("cbxLink1"))
        self.gridLayout_3.addWidget(self.cbxLink1, 1, 0, 1, 1)
        self.cboLink1 = QtGui.QComboBox(self.gbxLink)
        self.cboLink1.setObjectName(_fromUtf8("cboLink1"))
        self.gridLayout_3.addWidget(self.cboLink1, 1, 1, 1, 1)
        self.txtLink1 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink1.setObjectName(_fromUtf8("txtLink1"))
        self.gridLayout_3.addWidget(self.txtLink1, 1, 2, 1, 1)
        self.txtLink10 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink10.setObjectName(_fromUtf8("txtLink10"))
        self.gridLayout_3.addWidget(self.txtLink10, 1, 3, 1, 1)
        self.cbxLink2 = QtGui.QCheckBox(self.gbxLink)
        self.cbxLink2.setObjectName(_fromUtf8("cbxLink2"))
        self.gridLayout_3.addWidget(self.cbxLink2, 2, 0, 1, 1)
        self.cboLink2 = QtGui.QComboBox(self.gbxLink)
        self.cboLink2.setObjectName(_fromUtf8("cboLink2"))
        self.gridLayout_3.addWidget(self.cboLink2, 2, 1, 1, 1)
        self.txtLink2 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink2.setObjectName(_fromUtf8("txtLink2"))
        self.gridLayout_3.addWidget(self.txtLink2, 2, 2, 1, 1)
        self.txtLink11 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink11.setObjectName(_fromUtf8("txtLink11"))
        self.gridLayout_3.addWidget(self.txtLink11, 2, 3, 1, 1)
        self.cbxLink3 = QtGui.QCheckBox(self.gbxLink)
        self.cbxLink3.setObjectName(_fromUtf8("cbxLink3"))
        self.gridLayout_3.addWidget(self.cbxLink3, 3, 0, 1, 1)
        self.cboLink3 = QtGui.QComboBox(self.gbxLink)
        self.cboLink3.setObjectName(_fromUtf8("cboLink3"))
        self.gridLayout_3.addWidget(self.cboLink3, 3, 1, 1, 1)
        self.txtLink3 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink3.setObjectName(_fromUtf8("txtLink3"))
        self.gridLayout_3.addWidget(self.txtLink3, 3, 2, 1, 1)
        self.txtLink12 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink12.setObjectName(_fromUtf8("txtLink12"))
        self.gridLayout_3.addWidget(self.txtLink12, 3, 3, 1, 1)
        self.cbxLink4 = QtGui.QCheckBox(self.gbxLink)
        self.cbxLink4.setObjectName(_fromUtf8("cbxLink4"))
        self.gridLayout_3.addWidget(self.cbxLink4, 4, 0, 1, 1)
        self.cboLink4 = QtGui.QComboBox(self.gbxLink)
        self.cboLink4.setObjectName(_fromUtf8("cboLink4"))
        self.gridLayout_3.addWidget(self.cboLink4, 4, 1, 1, 1)
        self.txtLink4 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink4.setObjectName(_fromUtf8("txtLink4"))
        self.gridLayout_3.addWidget(self.txtLink4, 4, 2, 1, 1)
        self.txtLink13 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink13.setObjectName(_fromUtf8("txtLink13"))
        self.gridLayout_3.addWidget(self.txtLink13, 4, 3, 1, 1)
        self.cbxLink5 = QtGui.QCheckBox(self.gbxLink)
        self.cbxLink5.setObjectName(_fromUtf8("cbxLink5"))
        self.gridLayout_3.addWidget(self.cbxLink5, 5, 0, 1, 1)
        self.cboLink5 = QtGui.QComboBox(self.gbxLink)
        self.cboLink5.setObjectName(_fromUtf8("cboLink5"))
        self.gridLayout_3.addWidget(self.cboLink5, 5, 1, 1, 1)
        self.txtLink5 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink5.setObjectName(_fromUtf8("txtLink5"))
        self.gridLayout_3.addWidget(self.txtLink5, 5, 2, 1, 1)
        self.txtLink14 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink14.setObjectName(_fromUtf8("txtLink14"))
        self.gridLayout_3.addWidget(self.txtLink14, 5, 3, 1, 1)
        self.cbxLink6 = QtGui.QCheckBox(self.gbxLink)
        self.cbxLink6.setObjectName(_fromUtf8("cbxLink6"))
        self.gridLayout_3.addWidget(self.cbxLink6, 6, 0, 1, 1)
        self.cboLink6 = QtGui.QComboBox(self.gbxLink)
        self.cboLink6.setObjectName(_fromUtf8("cboLink6"))
        self.gridLayout_3.addWidget(self.cboLink6, 6, 1, 1, 1)
        self.txtLink6 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink6.setObjectName(_fromUtf8("txtLink6"))
        self.gridLayout_3.addWidget(self.txtLink6, 6, 2, 1, 1)
        self.txtLink15 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink15.setObjectName(_fromUtf8("txtLink15"))
        self.gridLayout_3.addWidget(self.txtLink15, 6, 3, 1, 1)
        self.cbxLink7 = QtGui.QCheckBox(self.gbxLink)
        self.cbxLink7.setObjectName(_fromUtf8("cbxLink7"))
        self.gridLayout_3.addWidget(self.cbxLink7, 7, 0, 1, 1)
        self.cboLink7 = QtGui.QComboBox(self.gbxLink)
        self.cboLink7.setObjectName(_fromUtf8("cboLink7"))
        self.gridLayout_3.addWidget(self.cboLink7, 7, 1, 1, 1)
        self.txtLink7 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink7.setObjectName(_fromUtf8("txtLink7"))
        self.gridLayout_3.addWidget(self.txtLink7, 7, 2, 1, 1)
        self.txtLink16 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink16.setObjectName(_fromUtf8("txtLink16"))
        self.gridLayout_3.addWidget(self.txtLink16, 7, 3, 1, 1)
        self.cbxLink8 = QtGui.QCheckBox(self.gbxLink)
        self.cbxLink8.setObjectName(_fromUtf8("cbxLink8"))
        self.gridLayout_3.addWidget(self.cbxLink8, 8, 0, 1, 1)
        self.cboLink8 = QtGui.QComboBox(self.gbxLink)
        self.cboLink8.setObjectName(_fromUtf8("cboLink8"))
        self.gridLayout_3.addWidget(self.cboLink8, 8, 1, 1, 1)
        self.txtLink8 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink8.setObjectName(_fromUtf8("txtLink8"))
        self.gridLayout_3.addWidget(self.txtLink8, 8, 2, 1, 1)
        self.txtLink17 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink17.setObjectName(_fromUtf8("txtLink17"))
        self.gridLayout_3.addWidget(self.txtLink17, 8, 3, 1, 1)
        self.cbxLink9 = QtGui.QCheckBox(self.gbxLink)
        self.cbxLink9.setObjectName(_fromUtf8("cbxLink9"))
        self.gridLayout_3.addWidget(self.cbxLink9, 9, 0, 1, 1)
        self.cboLink9 = QtGui.QComboBox(self.gbxLink)
        self.cboLink9.setObjectName(_fromUtf8("cboLink9"))
        self.gridLayout_3.addWidget(self.cboLink9, 9, 1, 1, 1)
        self.txtLink9 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink9.setObjectName(_fromUtf8("txtLink9"))
        self.gridLayout_3.addWidget(self.txtLink9, 9, 2, 1, 1)
        self.txtLink18 = QtGui.QLineEdit(self.gbxLink)
        self.txtLink18.setObjectName(_fromUtf8("txtLink18"))
        self.gridLayout_3.addWidget(self.txtLink18, 9, 3, 1, 1)
        self.verticalLayout.addWidget(self.gbxLink)
        self.fraOKCancel = QtGui.QFrame(self.centralWidget)
        self.fraOKCancel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraOKCancel.setFrameShadow(QtGui.QFrame.Raised)
        self.fraOKCancel.setObjectName(_fromUtf8("fraOKCancel"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.fraOKCancel)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem4 = QtGui.QSpacerItem(183, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.cmdOK = QtGui.QPushButton(self.fraOKCancel)
        self.cmdOK.setObjectName(_fromUtf8("cmdOK"))
        self.horizontalLayout.addWidget(self.cmdOK)
        self.cmdCancel = QtGui.QPushButton(self.fraOKCancel)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.verticalLayout.addWidget(self.fraOKCancel)
        frmReportOptions.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmReportOptions)
        QtCore.QMetaObject.connectSlotsByName(frmReportOptions)

    def retranslateUi(self, frmReportOptions):
        frmReportOptions.setWindowTitle(_translate("frmReportOptions", "EPANET Report Options", None))
        self.lblPageSize.setText(_translate("frmReportOptions", "Page Size", None))
        self.lblReportFileName.setText(_translate("frmReportOptions", "<html><head/><body><p>Report File Name</p></body></html>", None))
        self.lblStatus.setText(_translate("frmReportOptions", "Status", None))
        self.lblSummary.setText(_translate("frmReportOptions", "Summary", None))
        self.lblEnergy.setText(_translate("frmReportOptions", "Energy", None))
        self.gbxNode.setTitle(_translate("frmReportOptions", "Node Parameters:", None))
        self.lblLimit.setText(_translate("frmReportOptions", "Limit", None))
        self.lblPrecision.setText(_translate("frmReportOptions", "Precision", None))
        self.cbxNode1.setText(_translate("frmReportOptions", "Elevation", None))
        self.cbxNode2.setText(_translate("frmReportOptions", "Demand", None))
        self.cbxNode3.setText(_translate("frmReportOptions", "Head", None))
        self.cbxNode4.setText(_translate("frmReportOptions", "Pressure", None))
        self.cbxNode5.setText(_translate("frmReportOptions", "Quality", None))
        self.gbxLink.setTitle(_translate("frmReportOptions", "Link Parameters:", None))
        self.lblLimitLink.setText(_translate("frmReportOptions", "Limit", None))
        self.lblPrecisionLink.setText(_translate("frmReportOptions", "Precision", None))
        self.cbxLink1.setText(_translate("frmReportOptions", "Length", None))
        self.cbxLink2.setText(_translate("frmReportOptions", "Diameter", None))
        self.cbxLink3.setText(_translate("frmReportOptions", "Flow", None))
        self.cbxLink4.setText(_translate("frmReportOptions", "Velocity", None))
        self.cbxLink5.setText(_translate("frmReportOptions", "Headloss", None))
        self.cbxLink6.setText(_translate("frmReportOptions", "Position", None))
        self.cbxLink7.setText(_translate("frmReportOptions", "Setting", None))
        self.cbxLink8.setText(_translate("frmReportOptions", "Reaction", None))
        self.cbxLink9.setText(_translate("frmReportOptions", "F-Factor", None))
        self.cmdOK.setText(_translate("frmReportOptions", "OK", None))
        self.cmdCancel.setText(_translate("frmReportOptions", "Cancel", None))
