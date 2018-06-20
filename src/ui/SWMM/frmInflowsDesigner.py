# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dev\Python\dev-ui\src\ui\SWMM\frmInflowsDesigner.ui'
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

class Ui_frmInflows(object):
    def setupUi(self, frmInflows):
        frmInflows.setObjectName(_fromUtf8("frmInflows"))
        frmInflows.resize(397, 491)
        font = QFont()
        font.setPointSize(10)
        frmInflows.setFont(font)
        self.centralWidget = QWidget(frmInflows)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_2 = QVBoxLayout(self.centralWidget)
        # self.verticalLayout_2.setMargin(11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.fraTop = QFrame(self.centralWidget)
        self.fraTop.setFrameShape(QFrame.StyledPanel)
        self.fraTop.setFrameShadow(QFrame.Raised)
        self.fraTop.setObjectName(_fromUtf8("fraTop"))
        self.verticalLayout = QVBoxLayout(self.fraTop)
        # self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabInflows = QTabWidget(self.fraTop)
        self.tabInflows.setObjectName(_fromUtf8("tabInflows"))
        self.tabDirect = QWidget()
        self.tabDirect.setObjectName(_fromUtf8("tabDirect"))
        self.verticalLayout_3 = QVBoxLayout(self.tabDirect)
        # self.verticalLayout_3.setMargin(11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lblInflow = QLabel(self.tabDirect)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblInflow.sizePolicy().hasHeightForWidth())
        self.lblInflow.setSizePolicy(sizePolicy)
        self.lblInflow.setMaximumSize(QtCore.QSize(16777215, 70))
        self.lblInflow.setWordWrap(False)
        self.lblInflow.setObjectName(_fromUtf8("lblInflow"))
        self.verticalLayout_3.addWidget(self.lblInflow)
        self.fraDirect = QFrame(self.tabDirect)
        self.fraDirect.setFrameShape(QFrame.StyledPanel)
        self.fraDirect.setFrameShadow(QFrame.Raised)
        self.fraDirect.setObjectName(_fromUtf8("fraDirect"))
        self.gridLayout = QGridLayout(self.fraDirect)
        # self.gridLayout.setMargin(11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblConstituent = QLabel(self.fraDirect)
        self.lblConstituent.setObjectName(_fromUtf8("lblConstituent"))
        self.gridLayout.addWidget(self.lblConstituent, 0, 0, 1, 1)
        self.cboConstituent = QComboBox(self.fraDirect)
        self.cboConstituent.setObjectName(_fromUtf8("cboConstituent"))
        self.gridLayout.addWidget(self.cboConstituent, 0, 1, 1, 1)
        self.lblBaseline = QLabel(self.fraDirect)
        self.lblBaseline.setObjectName(_fromUtf8("lblBaseline"))
        self.gridLayout.addWidget(self.lblBaseline, 1, 0, 1, 1)
        self.txtBaseline = QLineEdit(self.fraDirect)
        self.txtBaseline.setObjectName(_fromUtf8("txtBaseline"))
        self.gridLayout.addWidget(self.txtBaseline, 1, 1, 1, 1)
        self.btnBaseline = QToolButton(self.fraDirect)
        self.btnBaseline.setObjectName(_fromUtf8("btnBaseline"))
        self.gridLayout.addWidget(self.btnBaseline, 1, 2, 1, 1)
        self.lblBaselinePattern = QLabel(self.fraDirect)
        self.lblBaselinePattern.setObjectName(_fromUtf8("lblBaselinePattern"))
        self.gridLayout.addWidget(self.lblBaselinePattern, 2, 0, 1, 1)
        self.cboPattern = QComboBox(self.fraDirect)
        self.cboPattern.setObjectName(_fromUtf8("cboPattern"))
        self.gridLayout.addWidget(self.cboPattern, 2, 1, 1, 1)
        self.btnPattern = QToolButton(self.fraDirect)
        self.btnPattern.setObjectName(_fromUtf8("btnPattern"))
        self.gridLayout.addWidget(self.btnPattern, 2, 2, 1, 1)
        self.btnPatternDelete = QToolButton(self.fraDirect)
        self.btnPatternDelete.setObjectName(_fromUtf8("btnPatternDelete"))
        self.gridLayout.addWidget(self.btnPatternDelete, 2, 3, 1, 1)
        self.lblTimeseries = QLabel(self.fraDirect)
        self.lblTimeseries.setObjectName(_fromUtf8("lblTimeseries"))
        self.gridLayout.addWidget(self.lblTimeseries, 3, 0, 1, 1)
        self.cboTimeSeries = QComboBox(self.fraDirect)
        self.cboTimeSeries.setObjectName(_fromUtf8("cboTimeSeries"))
        self.gridLayout.addWidget(self.cboTimeSeries, 3, 1, 1, 1)
        self.btnTimeseries = QToolButton(self.fraDirect)
        self.btnTimeseries.setObjectName(_fromUtf8("btnTimeseries"))
        self.gridLayout.addWidget(self.btnTimeseries, 3, 2, 1, 1)
        self.btnTimeseriesDelete = QToolButton(self.fraDirect)
        self.btnTimeseriesDelete.setObjectName(_fromUtf8("btnTimeseriesDelete"))
        self.gridLayout.addWidget(self.btnTimeseriesDelete, 3, 3, 1, 1)
        self.lblScaleFactor = QLabel(self.fraDirect)
        self.lblScaleFactor.setObjectName(_fromUtf8("lblScaleFactor"))
        self.gridLayout.addWidget(self.lblScaleFactor, 4, 0, 1, 1)
        self.txtScaleFactor = QLineEdit(self.fraDirect)
        self.txtScaleFactor.setObjectName(_fromUtf8("txtScaleFactor"))
        self.gridLayout.addWidget(self.txtScaleFactor, 4, 1, 1, 1)
        self.lblInflowType = QLabel(self.fraDirect)
        self.lblInflowType.setObjectName(_fromUtf8("lblInflowType"))
        self.gridLayout.addWidget(self.lblInflowType, 5, 0, 1, 1)
        self.cboInflowType = QComboBox(self.fraDirect)
        self.cboInflowType.setObjectName(_fromUtf8("cboInflowType"))
        self.gridLayout.addWidget(self.cboInflowType, 5, 1, 1, 1)
        self.lblUnitsFactor = QLabel(self.fraDirect)
        self.lblUnitsFactor.setObjectName(_fromUtf8("lblUnitsFactor"))
        self.gridLayout.addWidget(self.lblUnitsFactor, 6, 0, 1, 1)
        self.txtUnitsFactor = QLineEdit(self.fraDirect)
        self.txtUnitsFactor.setObjectName(_fromUtf8("txtUnitsFactor"))
        self.gridLayout.addWidget(self.txtUnitsFactor, 6, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.fraDirect)
        self.tabInflows.addTab(self.tabDirect, _fromUtf8(""))
        self.tabDry = QWidget()
        self.tabDry.setObjectName(_fromUtf8("tabDry"))
        self.verticalLayout_5 = QVBoxLayout(self.tabDry)
        # self.verticalLayout_5.setMargin(11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.lblInflow2 = QLabel(self.tabDry)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblInflow2.sizePolicy().hasHeightForWidth())
        self.lblInflow2.setSizePolicy(sizePolicy)
        self.lblInflow2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.lblInflow2.setWordWrap(False)
        self.lblInflow2.setObjectName(_fromUtf8("lblInflow2"))
        self.verticalLayout_5.addWidget(self.lblInflow2)
        self.fraDry = QFrame(self.tabDry)
        self.fraDry.setFrameShape(QFrame.StyledPanel)
        self.fraDry.setFrameShadow(QFrame.Raised)
        self.fraDry.setObjectName(_fromUtf8("fraDry"))
        self.gridLayout_2 = QGridLayout(self.fraDry)
        # self.gridLayout_2.setMargin(11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lblDryConstituent = QLabel(self.fraDry)
        self.lblDryConstituent.setObjectName(_fromUtf8("lblDryConstituent"))
        self.gridLayout_2.addWidget(self.lblDryConstituent, 0, 0, 1, 1)
        self.cboDryConstituent = QComboBox(self.fraDry)
        self.cboDryConstituent.setObjectName(_fromUtf8("cboDryConstituent"))
        self.gridLayout_2.addWidget(self.cboDryConstituent, 0, 1, 1, 1)
        self.lblAverage = QLabel(self.fraDry)
        self.lblAverage.setObjectName(_fromUtf8("lblAverage"))
        self.gridLayout_2.addWidget(self.lblAverage, 1, 0, 1, 1)
        self.txtAverage = QLineEdit(self.fraDry)
        self.txtAverage.setObjectName(_fromUtf8("txtAverage"))
        self.gridLayout_2.addWidget(self.txtAverage, 1, 1, 1, 1)
        self.btnAverage = QToolButton(self.fraDry)
        self.btnAverage.setObjectName(_fromUtf8("btnAverage"))
        self.gridLayout_2.addWidget(self.btnAverage, 1, 3, 1, 1)
        self.lblPatterns = QLabel(self.fraDry)
        self.lblPatterns.setObjectName(_fromUtf8("lblPatterns"))
        self.gridLayout_2.addWidget(self.lblPatterns, 2, 0, 1, 1)
        self.cboDryPattern1 = QComboBox(self.fraDry)
        self.cboDryPattern1.setObjectName(_fromUtf8("cboDryPattern1"))
        self.gridLayout_2.addWidget(self.cboDryPattern1, 2, 1, 1, 1)
        self.btnDryPattern1 = QToolButton(self.fraDry)
        self.btnDryPattern1.setObjectName(_fromUtf8("btnDryPattern1"))
        self.gridLayout_2.addWidget(self.btnDryPattern1, 2, 3, 1, 1)
        self.btnDryPattern5 = QToolButton(self.fraDry)
        self.btnDryPattern5.setObjectName(_fromUtf8("btnDryPattern5"))
        self.gridLayout_2.addWidget(self.btnDryPattern5, 2, 4, 1, 1)
        self.cboDryPattern2 = QComboBox(self.fraDry)
        self.cboDryPattern2.setObjectName(_fromUtf8("cboDryPattern2"))
        self.gridLayout_2.addWidget(self.cboDryPattern2, 3, 1, 1, 1)
        self.btnDryPattern3 = QToolButton(self.fraDry)
        self.btnDryPattern3.setObjectName(_fromUtf8("btnDryPattern3"))
        self.gridLayout_2.addWidget(self.btnDryPattern3, 4, 3, 1, 1)
        self.btnDryPattern7 = QToolButton(self.fraDry)
        self.btnDryPattern7.setObjectName(_fromUtf8("btnDryPattern7"))
        self.gridLayout_2.addWidget(self.btnDryPattern7, 4, 4, 1, 1)
        self.btnDryPattern6 = QToolButton(self.fraDry)
        self.btnDryPattern6.setObjectName(_fromUtf8("btnDryPattern6"))
        self.gridLayout_2.addWidget(self.btnDryPattern6, 3, 4, 1, 1)
        self.btnDryPattern2 = QToolButton(self.fraDry)
        self.btnDryPattern2.setObjectName(_fromUtf8("btnDryPattern2"))
        self.gridLayout_2.addWidget(self.btnDryPattern2, 3, 3, 1, 1)
        self.cboDryPattern3 = QComboBox(self.fraDry)
        self.cboDryPattern3.setObjectName(_fromUtf8("cboDryPattern3"))
        self.gridLayout_2.addWidget(self.cboDryPattern3, 4, 1, 1, 1)
        self.cboDryPattern4 = QComboBox(self.fraDry)
        self.cboDryPattern4.setObjectName(_fromUtf8("cboDryPattern4"))
        self.gridLayout_2.addWidget(self.cboDryPattern4, 5, 1, 1, 1)
        self.btnDryPattern4 = QToolButton(self.fraDry)
        self.btnDryPattern4.setObjectName(_fromUtf8("btnDryPattern4"))
        self.gridLayout_2.addWidget(self.btnDryPattern4, 5, 3, 1, 1)
        self.btnDryPattern8 = QToolButton(self.fraDry)
        self.btnDryPattern8.setObjectName(_fromUtf8("btnDryPattern8"))
        self.gridLayout_2.addWidget(self.btnDryPattern8, 5, 4, 1, 1)
        self.verticalLayout_5.addWidget(self.fraDry)
        self.tabInflows.addTab(self.tabDry, _fromUtf8(""))
        self.tabRdii = QWidget()
        self.tabRdii.setObjectName(_fromUtf8("tabRdii"))
        self.verticalLayout_6 = QVBoxLayout(self.tabRdii)
        # self.verticalLayout_6.setMargin(11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.fraUpper = QFrame(self.tabRdii)
        self.fraUpper.setFrameShape(QFrame.StyledPanel)
        self.fraUpper.setFrameShadow(QFrame.Raised)
        self.fraUpper.setObjectName(_fromUtf8("fraUpper"))
        self.gridLayout_3 = QGridLayout(self.fraUpper)
        # self.gridLayout_3.setMargin(11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lblUnitHydro = QLabel(self.fraUpper)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblUnitHydro.sizePolicy().hasHeightForWidth())
        self.lblUnitHydro.setSizePolicy(sizePolicy)
        self.lblUnitHydro.setObjectName(_fromUtf8("lblUnitHydro"))
        self.gridLayout_3.addWidget(self.lblUnitHydro, 0, 0, 1, 2)
        self.cboUnitHydro = QComboBox(self.fraUpper)
        self.cboUnitHydro.setObjectName(_fromUtf8("cboUnitHydro"))
        self.gridLayout_3.addWidget(self.cboUnitHydro, 1, 0, 1, 1)
        self.btnUnitHydro1 = QToolButton(self.fraUpper)
        self.btnUnitHydro1.setObjectName(_fromUtf8("btnUnitHydro1"))
        self.gridLayout_3.addWidget(self.btnUnitHydro1, 1, 1, 1, 1)
        self.btnUniHydro2 = QToolButton(self.fraUpper)
        self.btnUniHydro2.setObjectName(_fromUtf8("btnUniHydro2"))
        self.gridLayout_3.addWidget(self.btnUniHydro2, 1, 2, 1, 1)
        self.verticalLayout_6.addWidget(self.fraUpper)
        self.fraLower = QFrame(self.tabRdii)
        self.fraLower.setFrameShape(QFrame.StyledPanel)
        self.fraLower.setFrameShadow(QFrame.Raised)
        self.fraLower.setObjectName(_fromUtf8("fraLower"))
        self.horizontalLayout_2 = QHBoxLayout(self.fraLower)
        # self.horizontalLayout_2.setMargin(11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblSewershed = QLabel(self.fraLower)
        self.lblSewershed.setWordWrap(True)
        self.lblSewershed.setObjectName(_fromUtf8("lblSewershed"))
        self.horizontalLayout_2.addWidget(self.lblSewershed)
        self.txtSewershed = QLineEdit(self.fraLower)
        self.txtSewershed.setObjectName(_fromUtf8("txtSewershed"))
        self.horizontalLayout_2.addWidget(self.txtSewershed)
        self.verticalLayout_6.addWidget(self.fraLower)
        self.tabInflows.addTab(self.tabRdii, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabInflows)
        self.verticalLayout_2.addWidget(self.fraTop)
        self.gbxNotes = QGroupBox(self.centralWidget)
        self.gbxNotes.setTitle(_fromUtf8(""))
        self.gbxNotes.setObjectName(_fromUtf8("gbxNotes"))
        self.verticalLayout_4 = QVBoxLayout(self.gbxNotes)
        # self.verticalLayout_4.setMargin(11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lblNotes = QLabel(self.gbxNotes)
        self.lblNotes.setWordWrap(True)
        self.lblNotes.setObjectName(_fromUtf8("lblNotes"))
        self.verticalLayout_4.addWidget(self.lblNotes)
        self.verticalLayout_2.addWidget(self.gbxNotes)
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
        self.verticalLayout_2.addWidget(self.fraOKCancel)
        frmInflows.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmInflows)
        self.tabInflows.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmInflows)

    def retranslateUi(self, frmInflows):
        frmInflows.setWindowTitle(_translate("frmInflows", "SWMM Inflows", None))
        self.lblInflow.setText(_translate("frmInflows", "Inflow = (Baseline Value) x (Baseline Pattern) +       \n"
"          (Time Series Value) x (Scale Factor)", None))
        self.lblConstituent.setText(_translate("frmInflows", "Constituent", None))
        self.lblBaseline.setText(_translate("frmInflows", "Baseline", None))
        self.btnBaseline.setText(_translate("frmInflows", "X", None))
        self.lblBaselinePattern.setText(_translate("frmInflows", "Baseline Pattern", None))
        self.btnPattern.setText(_translate("frmInflows", "...", None))
        self.btnPatternDelete.setText(_translate("frmInflows", "X", None))
        self.lblTimeseries.setText(_translate("frmInflows", "Time Series", None))
        self.btnTimeseries.setText(_translate("frmInflows", "...", None))
        self.btnTimeseriesDelete.setText(_translate("frmInflows", "X", None))
        self.lblScaleFactor.setText(_translate("frmInflows", "Scale Factor", None))
        self.lblInflowType.setText(_translate("frmInflows", "Inflow Type", None))
        self.lblUnitsFactor.setText(_translate("frmInflows", "Units Factor", None))
        self.tabInflows.setTabText(self.tabInflows.indexOf(self.tabDirect), _translate("frmInflows", "Direct", None))
        self.lblInflow2.setText(_translate("frmInflows", "Inflow = (Average Value) x (Pattern 1) x       \n"
"          (Pattern 2) x (Pattern 3) x (Pattern 4)", None))
        self.lblDryConstituent.setText(_translate("frmInflows", "Constituent", None))
        self.lblAverage.setText(_translate("frmInflows", "Average Value", None))
        self.btnAverage.setText(_translate("frmInflows", "X", None))
        self.lblPatterns.setText(_translate("frmInflows", "Time Patterns", None))
        self.btnDryPattern1.setText(_translate("frmInflows", "...", None))
        self.btnDryPattern5.setText(_translate("frmInflows", "X", None))
        self.btnDryPattern3.setText(_translate("frmInflows", "...", None))
        self.btnDryPattern7.setText(_translate("frmInflows", "X", None))
        self.btnDryPattern6.setText(_translate("frmInflows", "X", None))
        self.btnDryPattern2.setText(_translate("frmInflows", "...", None))
        self.btnDryPattern4.setText(_translate("frmInflows", "...", None))
        self.btnDryPattern8.setText(_translate("frmInflows", "X", None))
        self.tabInflows.setTabText(self.tabInflows.indexOf(self.tabDry), _translate("frmInflows", "Dry Weather", None))
        self.lblUnitHydro.setText(_translate("frmInflows", "Unit Hydrograph Group", None))
        self.btnUnitHydro1.setText(_translate("frmInflows", "...", None))
        self.btnUniHydro2.setText(_translate("frmInflows", "X", None))
        self.lblSewershed.setText(_translate("frmInflows", "Seweshed Area (acres)", None))
        self.tabInflows.setTabText(self.tabInflows.indexOf(self.tabRdii), _translate("frmInflows", "RDII", None))
        self.lblNotes.setText(_translate("frmInflows", "<html><head/><body><p>If Baseline or Time Series is left blank its value is 0. If Baseline Pattern is left blank its value is 1.0.</p></body></html>", None))
        self.cmdOK.setText(_translate("frmInflows", "OK", None))
        self.cmdCancel.setText(_translate("frmInflows", "Cancel", None))

