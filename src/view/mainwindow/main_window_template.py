# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_template.ui'
#
# Created: Sat Jan 02 20:44:25 2010
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EIVFmxEREd-LgJ4IxcJkTA
    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 345)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.AssetViewerButton = QtGui.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/64_64/icon07_13.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AssetViewerButton.setIcon(icon)
        self.AssetViewerButton.setIconSize(QtCore.QSize(64, 64))
        self.AssetViewerButton.setObjectName("AssetViewerButton")
        self.verticalLayout.addWidget(self.AssetViewerButton)
        self.AssetViewerLabel = QtGui.QLabel(self.centralwidget)
        self.AssetViewerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AssetViewerLabel.setObjectName("AssetViewerLabel")
        self.verticalLayout.addWidget(self.AssetViewerLabel)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.CharacterViewerButton = QtGui.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/64_64/icon02_16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CharacterViewerButton.setIcon(icon1)
        self.CharacterViewerButton.setIconSize(QtCore.QSize(64, 64))
        self.CharacterViewerButton.setObjectName("CharacterViewerButton")
        self.verticalLayout_3.addWidget(self.CharacterViewerButton)
        self.CharacterViewerLabel = QtGui.QLabel(self.centralwidget)
        self.CharacterViewerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CharacterViewerLabel.setObjectName("CharacterViewerLabel")
        self.verticalLayout_3.addWidget(self.CharacterViewerLabel)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ShipFitterButton = QtGui.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/64_64/icon17_04.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ShipFitterButton.setIcon(icon2)
        self.ShipFitterButton.setIconSize(QtCore.QSize(64, 64))
        self.ShipFitterButton.setObjectName("ShipFitterButton")
        self.verticalLayout_2.addWidget(self.ShipFitterButton)
        self.ShipFitterLabel = QtGui.QLabel(self.centralwidget)
        self.ShipFitterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ShipFitterLabel.setObjectName("ShipFitterLabel")
        self.verticalLayout_2.addWidget(self.ShipFitterLabel)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ItemBrowserButton = QtGui.QPushButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/64_64/icon61_04.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ItemBrowserButton.setIcon(icon3)
        self.ItemBrowserButton.setIconSize(QtCore.QSize(64, 64))
        self.ItemBrowserButton.setObjectName("ItemBrowserButton")
        self.verticalLayout_4.addWidget(self.ItemBrowserButton)
        self.ItemBrowserLabel = QtGui.QLabel(self.centralwidget)
        self.ItemBrowserLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ItemBrowserLabel.setObjectName("ItemBrowserLabel")
        self.verticalLayout_4.addWidget(self.ItemBrowserLabel)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 3, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ManufacturingCalculatorButton = QtGui.QPushButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/64_64/icon18_02.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ManufacturingCalculatorButton.setIcon(icon4)
        self.ManufacturingCalculatorButton.setIconSize(QtCore.QSize(64, 64))
        self.ManufacturingCalculatorButton.setObjectName("ManufacturingCalculatorButton")
        self.verticalLayout_5.addWidget(self.ManufacturingCalculatorButton)
        self.ManufacturingCalculatorLabel = QtGui.QLabel(self.centralwidget)
        self.ManufacturingCalculatorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ManufacturingCalculatorLabel.setObjectName("ManufacturingCalculatorLabel")
        self.verticalLayout_5.addWidget(self.ManufacturingCalculatorLabel)
        self.gridLayout.addLayout(self.verticalLayout_5, 1, 0, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.MiningCalculatorButton = QtGui.QPushButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/64_64/icon67_02.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MiningCalculatorButton.setIcon(icon5)
        self.MiningCalculatorButton.setIconSize(QtCore.QSize(64, 64))
        self.MiningCalculatorButton.setObjectName("MiningCalculatorButton")
        self.verticalLayout_6.addWidget(self.MiningCalculatorButton)
        self.MiningCalculatorLabel = QtGui.QLabel(self.centralwidget)
        self.MiningCalculatorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MiningCalculatorLabel.setObjectName("MiningCalculatorLabel")
        self.verticalLayout_6.addWidget(self.MiningCalculatorLabel)
        self.gridLayout.addLayout(self.verticalLayout_6, 1, 1, 1, 1)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.RefineCalculatorButton = QtGui.QPushButton(self.centralwidget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/64_64/icon32_02.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RefineCalculatorButton.setIcon(icon6)
        self.RefineCalculatorButton.setIconSize(QtCore.QSize(64, 64))
        self.RefineCalculatorButton.setObjectName("RefineCalculatorButton")
        self.verticalLayout_7.addWidget(self.RefineCalculatorButton)
        self.RefineCalculatorLabel = QtGui.QLabel(self.centralwidget)
        self.RefineCalculatorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RefineCalculatorLabel.setObjectName("RefineCalculatorLabel")
        self.verticalLayout_7.addWidget(self.RefineCalculatorLabel)
        self.gridLayout.addLayout(self.verticalLayout_7, 1, 2, 1, 1)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.ResearchCalculatorButton = QtGui.QPushButton(self.centralwidget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/64_64/icon57_09.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ResearchCalculatorButton.setIcon(icon7)
        self.ResearchCalculatorButton.setIconSize(QtCore.QSize(64, 64))
        self.ResearchCalculatorButton.setObjectName("ResearchCalculatorButton")
        self.verticalLayout_8.addWidget(self.ResearchCalculatorButton)
        self.ResearchCalculatorLabel = QtGui.QLabel(self.centralwidget)
        self.ResearchCalculatorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ResearchCalculatorLabel.setObjectName("ResearchCalculatorLabel")
        self.verticalLayout_8.addWidget(self.ResearchCalculatorLabel)
        self.gridLayout.addLayout(self.verticalLayout_8, 1, 3, 1, 1)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.POSFitterButton = QtGui.QPushButton(self.centralwidget)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/64_64/icon55_07.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.POSFitterButton.setIcon(icon8)
        self.POSFitterButton.setIconSize(QtCore.QSize(64, 64))
        self.POSFitterButton.setObjectName("POSFitterButton")
        self.verticalLayout_12.addWidget(self.POSFitterButton)
        self.POSFitterLabel = QtGui.QLabel(self.centralwidget)
        self.POSFitterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.POSFitterLabel.setObjectName("POSFitterLabel")
        self.verticalLayout_12.addWidget(self.POSFitterLabel)
        self.gridLayout.addLayout(self.verticalLayout_12, 2, 0, 1, 1)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.SkillBrowserButton = QtGui.QPushButton(self.centralwidget)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/64_64/icon50_14.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SkillBrowserButton.setIcon(icon9)
        self.SkillBrowserButton.setIconSize(QtCore.QSize(64, 64))
        self.SkillBrowserButton.setObjectName("SkillBrowserButton")
        self.verticalLayout_9.addWidget(self.SkillBrowserButton)
        self.SkillBrowserLabel = QtGui.QLabel(self.centralwidget)
        self.SkillBrowserLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SkillBrowserLabel.setObjectName("SkillBrowserLabel")
        self.verticalLayout_9.addWidget(self.SkillBrowserLabel)
        self.gridLayout.addLayout(self.verticalLayout_9, 2, 1, 1, 1)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.SkillPlannerButton = QtGui.QPushButton(self.centralwidget)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/64_64/icon36_15.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SkillPlannerButton.setIcon(icon10)
        self.SkillPlannerButton.setIconSize(QtCore.QSize(64, 64))
        self.SkillPlannerButton.setObjectName("SkillPlannerButton")
        self.verticalLayout_10.addWidget(self.SkillPlannerButton)
        self.SkillPlannerLabel = QtGui.QLabel(self.centralwidget)
        self.SkillPlannerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SkillPlannerLabel.setObjectName("SkillPlannerLabel")
        self.verticalLayout_10.addWidget(self.SkillPlannerLabel)
        self.gridLayout.addLayout(self.verticalLayout_10, 2, 2, 1, 1)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.TravelPlannerButton = QtGui.QPushButton(self.centralwidget)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/64_64/icon07_04.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TravelPlannerButton.setIcon(icon11)
        self.TravelPlannerButton.setIconSize(QtCore.QSize(64, 64))
        self.TravelPlannerButton.setObjectName("TravelPlannerButton")
        self.verticalLayout_11.addWidget(self.TravelPlannerButton)
        self.TravelPlannerLabel = QtGui.QLabel(self.centralwidget)
        self.TravelPlannerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TravelPlannerLabel.setObjectName("TravelPlannerLabel")
        self.verticalLayout_11.addWidget(self.TravelPlannerLabel)
        self.gridLayout.addLayout(self.verticalLayout_11, 2, 3, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.CharacterViewerButton, self.AssetViewerButton)
        MainWindow.setTabOrder(self.AssetViewerButton, self.ShipFitterButton)
        MainWindow.setTabOrder(self.ShipFitterButton, self.ItemBrowserButton)
        MainWindow.setTabOrder(self.ItemBrowserButton, self.ManufacturingCalculatorButton)
        MainWindow.setTabOrder(self.ManufacturingCalculatorButton, self.MiningCalculatorButton)
        MainWindow.setTabOrder(self.MiningCalculatorButton, self.RefineCalculatorButton)
        MainWindow.setTabOrder(self.RefineCalculatorButton, self.ResearchCalculatorButton)
        MainWindow.setTabOrder(self.ResearchCalculatorButton, self.POSFitterButton)
        MainWindow.setTabOrder(self.POSFitterButton, self.SkillBrowserButton)
        MainWindow.setTabOrder(self.SkillBrowserButton, self.SkillPlannerButton)
        MainWindow.setTabOrder(self.SkillPlannerButton, self.TravelPlannerButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "EVE Suite", None, QtGui.QApplication.UnicodeUTF8))
        self.AssetViewerLabel.setText(QtGui.QApplication.translate("MainWindow", "Asset Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.CharacterViewerLabel.setText(QtGui.QApplication.translate("MainWindow", "Character Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.ShipFitterLabel.setText(QtGui.QApplication.translate("MainWindow", "Ship Fitter", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemBrowserLabel.setText(QtGui.QApplication.translate("MainWindow", "Item Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.ManufacturingCalculatorLabel.setText(QtGui.QApplication.translate("MainWindow", "Manufacturing\n"
"Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.MiningCalculatorLabel.setText(QtGui.QApplication.translate("MainWindow", "Mining Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.RefineCalculatorLabel.setText(QtGui.QApplication.translate("MainWindow", "Refine Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.ResearchCalculatorLabel.setText(QtGui.QApplication.translate("MainWindow", "Research\n"
"Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.POSFitterLabel.setText(QtGui.QApplication.translate("MainWindow", "POS Fitter", None, QtGui.QApplication.UnicodeUTF8))
        self.SkillBrowserLabel.setText(QtGui.QApplication.translate("MainWindow", "Skill Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.SkillPlannerLabel.setText(QtGui.QApplication.translate("MainWindow", "Skill Planner", None, QtGui.QApplication.UnicodeUTF8))
        self.TravelPlannerLabel.setText(QtGui.QApplication.translate("MainWindow", "Travel Planner", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

import main_window_rc
