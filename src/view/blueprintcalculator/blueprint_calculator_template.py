# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Blueprint Calculator.ui'
#
# Created: Sun Dec  6 16:39:06 2009
#      by: PyQt4 UI code generator 4.6.2-snapshot-20091118
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 412)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelBlueprintSelection = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBlueprintSelection.sizePolicy().hasHeightForWidth())
        self.labelBlueprintSelection.setSizePolicy(sizePolicy)
        self.labelBlueprintSelection.setFrameShape(QtGui.QFrame.NoFrame)
        self.labelBlueprintSelection.setObjectName("labelBlueprintSelection")
        self.horizontalLayout.addWidget(self.labelBlueprintSelection)
        self.comboBluprintSelection = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBluprintSelection.sizePolicy().hasHeightForWidth())
        self.comboBluprintSelection.setSizePolicy(sizePolicy)
        self.comboBluprintSelection.setEditable(True)
        self.comboBluprintSelection.setObjectName("comboBluprintSelection")
        self.horizontalLayout.addWidget(self.comboBluprintSelection)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelME = QtGui.QLabel(self.groupBox)
        self.labelME.setObjectName("labelME")
        self.horizontalLayout_2.addWidget(self.labelME)
        self.spinME = QtGui.QSpinBox(self.groupBox)
        self.spinME.setMaximum(1000000)
        self.spinME.setObjectName("spinME")
        self.horizontalLayout_2.addWidget(self.spinME)
        self.labelPE = QtGui.QLabel(self.groupBox)
        self.labelPE.setObjectName("labelPE")
        self.horizontalLayout_2.addWidget(self.labelPE)
        self.spinPE = QtGui.QSpinBox(self.groupBox)
        self.spinPE.setMaximum(1000000)
        self.spinPE.setObjectName("spinPE")
        self.horizontalLayout_2.addWidget(self.spinPE)
        self.labelRuns = QtGui.QLabel(self.groupBox)
        self.labelRuns.setObjectName("labelRuns")
        self.horizontalLayout_2.addWidget(self.labelRuns)
        self.spinRuns = QtGui.QSpinBox(self.groupBox)
        self.spinRuns.setMaximum(1000000)
        self.spinRuns.setObjectName("spinRuns")
        self.horizontalLayout_2.addWidget(self.spinRuns)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelIndustry = QtGui.QLabel(self.groupBox_2)
        self.labelIndustry.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelIndustry.setObjectName("labelIndustry")
        self.gridLayout.addWidget(self.labelIndustry, 0, 0, 1, 1)
        self.labelProductionEfficiency = QtGui.QLabel(self.groupBox_2)
        self.labelProductionEfficiency.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelProductionEfficiency.setObjectName("labelProductionEfficiency")
        self.gridLayout.addWidget(self.labelProductionEfficiency, 1, 0, 1, 1)
        self.comboIndustry = QtGui.QComboBox(self.groupBox_2)
        self.comboIndustry.setObjectName("comboIndustry")
        self.gridLayout.addWidget(self.comboIndustry, 0, 1, 1, 1)
        self.comboProductionEfficiency = QtGui.QComboBox(self.groupBox_2)
        self.comboProductionEfficiency.setObjectName("comboProductionEfficiency")
        self.gridLayout.addWidget(self.comboProductionEfficiency, 1, 1, 1, 1)
        self.labelResearch = QtGui.QLabel(self.groupBox_2)
        self.labelResearch.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelResearch.setObjectName("labelResearch")
        self.gridLayout.addWidget(self.labelResearch, 1, 2, 1, 1)
        self.labelMetallurgy = QtGui.QLabel(self.groupBox_2)
        self.labelMetallurgy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelMetallurgy.setObjectName("labelMetallurgy")
        self.gridLayout.addWidget(self.labelMetallurgy, 0, 2, 1, 1)
        self.comboMetallurgy = QtGui.QComboBox(self.groupBox_2)
        self.comboMetallurgy.setObjectName("comboMetallurgy")
        self.gridLayout.addWidget(self.comboMetallurgy, 0, 3, 1, 1)
        self.comboResearch = QtGui.QComboBox(self.groupBox_2)
        self.comboResearch.setObjectName("comboResearch")
        self.gridLayout.addWidget(self.comboResearch, 1, 3, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tableMaterials = QtGui.QTableWidget(self.centralwidget)
        self.tableMaterials.setObjectName("tableMaterials")
        self.tableMaterials.setColumnCount(8)
        self.tableMaterials.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableMaterials.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableMaterials.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableMaterials.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableMaterials.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableMaterials.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableMaterials.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableMaterials.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableMaterials.setHorizontalHeaderItem(7, item)
        self.verticalLayout.addWidget(self.tableMaterials)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.labelBlueprintSelection.setBuddy(self.comboBluprintSelection)
        self.labelME.setBuddy(self.spinME)
        self.labelPE.setBuddy(self.spinPE)
        self.labelRuns.setBuddy(self.spinRuns)
        self.labelIndustry.setBuddy(self.comboIndustry)
        self.labelProductionEfficiency.setBuddy(self.comboProductionEfficiency)
        self.labelResearch.setBuddy(self.comboResearch)
        self.labelMetallurgy.setBuddy(self.comboMetallurgy)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Blueprint Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.labelBlueprintSelection.setText(QtGui.QApplication.translate("MainWindow", "Blueprint:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelME.setText(QtGui.QApplication.translate("MainWindow", "ME:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPE.setText(QtGui.QApplication.translate("MainWindow", "PE:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRuns.setText(QtGui.QApplication.translate("MainWindow", "Runs:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Skills", None, QtGui.QApplication.UnicodeUTF8))
        self.labelIndustry.setText(QtGui.QApplication.translate("MainWindow", "Industry:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelProductionEfficiency.setText(QtGui.QApplication.translate("MainWindow", "Production Efficiency:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelResearch.setText(QtGui.QApplication.translate("MainWindow", "Research:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMetallurgy.setText(QtGui.QApplication.translate("MainWindow", "Metallurgy:", None, QtGui.QApplication.UnicodeUTF8))
        self.tableMaterials.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableMaterials.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Base Amount", None, QtGui.QApplication.UnicodeUTF8))
        self.tableMaterials.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Waste", None, QtGui.QApplication.UnicodeUTF8))
        self.tableMaterials.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.tableMaterials.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "Unit Price", None, QtGui.QApplication.UnicodeUTF8))
        self.tableMaterials.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "Total Price", None, QtGui.QApplication.UnicodeUTF8))
        self.tableMaterials.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("MainWindow", "Perfect ME", None, QtGui.QApplication.UnicodeUTF8))
        self.tableMaterials.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("MainWindow", "Improve At Level", None, QtGui.QApplication.UnicodeUTF8))
