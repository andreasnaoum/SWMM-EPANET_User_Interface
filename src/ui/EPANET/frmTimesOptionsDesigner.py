# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EPANET\frmTimesOptionsDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmTimesOptions(object):
    def setupUi(self, frmTimesOptions):
        frmTimesOptions.setObjectName("frmTimesOptions")
        frmTimesOptions.resize(302, 440)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmTimesOptions.setFont(font)
        self.centralWidget = QtWidgets.QWidget(frmTimesOptions)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fraTop = QtWidgets.QFrame(self.centralWidget)
        self.fraTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraTop.setObjectName("fraTop")
        self.gridLayout = QtWidgets.QGridLayout(self.fraTop)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lblTotalDuration = QtWidgets.QLabel(self.fraTop)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblTotalDuration.setFont(font)
        self.lblTotalDuration.setObjectName("lblTotalDuration")
        self.gridLayout.addWidget(self.lblTotalDuration, 0, 0, 1, 1)
        self.txtTotalDuration = QtWidgets.QLineEdit(self.fraTop)
        self.txtTotalDuration.setObjectName("txtTotalDuration")
        self.gridLayout.addWidget(self.txtTotalDuration, 0, 1, 1, 1)
        self.lblHydraulic = QtWidgets.QLabel(self.fraTop)
        self.lblHydraulic.setObjectName("lblHydraulic")
        self.gridLayout.addWidget(self.lblHydraulic, 1, 0, 1, 1)
        self.txtHydraulic = QtWidgets.QLineEdit(self.fraTop)
        self.txtHydraulic.setObjectName("txtHydraulic")
        self.gridLayout.addWidget(self.txtHydraulic, 1, 1, 1, 1)
        self.lblQuality = QtWidgets.QLabel(self.fraTop)
        self.lblQuality.setObjectName("lblQuality")
        self.gridLayout.addWidget(self.lblQuality, 2, 0, 1, 1)
        self.txtQuality = QtWidgets.QLineEdit(self.fraTop)
        self.txtQuality.setObjectName("txtQuality")
        self.gridLayout.addWidget(self.txtQuality, 2, 1, 1, 1)
        self.lblRule = QtWidgets.QLabel(self.fraTop)
        self.lblRule.setObjectName("lblRule")
        self.gridLayout.addWidget(self.lblRule, 3, 0, 1, 1)
        self.txtRule = QtWidgets.QLineEdit(self.fraTop)
        self.txtRule.setObjectName("txtRule")
        self.gridLayout.addWidget(self.txtRule, 3, 1, 1, 1)
        self.lblPattern = QtWidgets.QLabel(self.fraTop)
        self.lblPattern.setObjectName("lblPattern")
        self.gridLayout.addWidget(self.lblPattern, 4, 0, 1, 1)
        self.txtPattern = QtWidgets.QLineEdit(self.fraTop)
        self.txtPattern.setObjectName("txtPattern")
        self.gridLayout.addWidget(self.txtPattern, 4, 1, 1, 1)
        self.lblPatternTime = QtWidgets.QLabel(self.fraTop)
        self.lblPatternTime.setObjectName("lblPatternTime")
        self.gridLayout.addWidget(self.lblPatternTime, 5, 0, 1, 1)
        self.txtPatternTime = QtWidgets.QLineEdit(self.fraTop)
        self.txtPatternTime.setObjectName("txtPatternTime")
        self.gridLayout.addWidget(self.txtPatternTime, 5, 1, 1, 1)
        self.lblReporting = QtWidgets.QLabel(self.fraTop)
        self.lblReporting.setObjectName("lblReporting")
        self.gridLayout.addWidget(self.lblReporting, 6, 0, 1, 1)
        self.txtReporting = QtWidgets.QLineEdit(self.fraTop)
        self.txtReporting.setObjectName("txtReporting")
        self.gridLayout.addWidget(self.txtReporting, 6, 1, 1, 1)
        self.lblReportingTime = QtWidgets.QLabel(self.fraTop)
        self.lblReportingTime.setObjectName("lblReportingTime")
        self.gridLayout.addWidget(self.lblReportingTime, 7, 0, 1, 1)
        self.txtReportingTime = QtWidgets.QLineEdit(self.fraTop)
        self.txtReportingTime.setObjectName("txtReportingTime")
        self.gridLayout.addWidget(self.txtReportingTime, 7, 1, 1, 1)
        self.lblClockStart = QtWidgets.QLabel(self.fraTop)
        self.lblClockStart.setObjectName("lblClockStart")
        self.gridLayout.addWidget(self.lblClockStart, 8, 0, 1, 1)
        self.txtClockStart = QtWidgets.QLineEdit(self.fraTop)
        self.txtClockStart.setObjectName("txtClockStart")
        self.gridLayout.addWidget(self.txtClockStart, 8, 1, 1, 1)
        self.lblStatistic = QtWidgets.QLabel(self.fraTop)
        self.lblStatistic.setObjectName("lblStatistic")
        self.gridLayout.addWidget(self.lblStatistic, 9, 0, 1, 1)
        self.cboStatistic = QtWidgets.QComboBox(self.fraTop)
        self.cboStatistic.setObjectName("cboStatistic")
        self.gridLayout.addWidget(self.cboStatistic, 9, 1, 1, 1)
        self.verticalLayout.addWidget(self.fraTop)
        self.fraOKCancel = QtWidgets.QFrame(self.centralWidget)
        self.fraOKCancel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraOKCancel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraOKCancel.setObjectName("fraOKCancel")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fraOKCancel)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(138, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cmdOK = QtWidgets.QPushButton(self.fraOKCancel)
        self.cmdOK.setObjectName("cmdOK")
        self.horizontalLayout.addWidget(self.cmdOK)
        self.cmdCancel = QtWidgets.QPushButton(self.fraOKCancel)
        self.cmdCancel.setObjectName("cmdCancel")
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.verticalLayout.addWidget(self.fraOKCancel)
        frmTimesOptions.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmTimesOptions)
        QtCore.QMetaObject.connectSlotsByName(frmTimesOptions)

    def retranslateUi(self, frmTimesOptions):
        _translate = QtCore.QCoreApplication.translate
        frmTimesOptions.setWindowTitle(_translate("frmTimesOptions", "EPANET Times Options"))
        self.lblTotalDuration.setText(_translate("frmTimesOptions", "Total Duration"))
        self.lblHydraulic.setText(_translate("frmTimesOptions", "<html><head/><body><p>Hydraulic Time Step</p></body></html>"))
        self.lblQuality.setText(_translate("frmTimesOptions", "Quality Time Step"))
        self.lblRule.setText(_translate("frmTimesOptions", "Rule Time Step"))
        self.lblPattern.setText(_translate("frmTimesOptions", "Pattern Time Step"))
        self.lblPatternTime.setText(_translate("frmTimesOptions", "Pattern Start Time"))
        self.lblReporting.setText(_translate("frmTimesOptions", "Reporting Time Step"))
        self.lblReportingTime.setText(_translate("frmTimesOptions", "Report Start Time"))
        self.lblClockStart.setText(_translate("frmTimesOptions", "Clock Start Time"))
        self.lblStatistic.setText(_translate("frmTimesOptions", "Statistic"))
        self.cmdOK.setText(_translate("frmTimesOptions", "OK"))
        self.cmdCancel.setText(_translate("frmTimesOptions", "Cancel"))

