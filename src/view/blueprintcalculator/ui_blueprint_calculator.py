# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_blueprint_calculator.ui'
#
# Created: Tue Apr 12 20:59:39 2011
#      by: pyside-uic 0.2.7 running on PySide 1.0.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_BlueprintCalculator(object):
    def setupUi(self, BlueprintCalculator):
        BlueprintCalculator.setObjectName("BlueprintCalculator")
        BlueprintCalculator.resize(801, 544)
        self.centralwidget = QtGui.QWidget(BlueprintCalculator)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.blueprint_combo = QtGui.QComboBox(self.groupBox)
        self.blueprint_combo.setEditable(True)
        self.blueprint_combo.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.blueprint_combo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.blueprint_combo.setObjectName("blueprint_combo")
        self.horizontalLayout_2.addWidget(self.blueprint_combo)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.character_combo = QtGui.QComboBox(self.groupBox_2)
        self.character_combo.setEditable(False)
        self.character_combo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.character_combo.setFrame(True)
        self.character_combo.setObjectName("character_combo")
        self.character_combo.addItem("")
        self.character_combo.addItem("")
        self.horizontalLayout_4.addWidget(self.character_combo)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.manufacturing_tree = QtGui.QTreeView(self.widget_2)
        self.manufacturing_tree.setObjectName("manufacturing_tree")
        self.horizontalLayout_3.addWidget(self.manufacturing_tree)
        self.blueprint_tree = QtGui.QTreeView(self.widget_2)
        self.blueprint_tree.setObjectName("blueprint_tree")
        self.horizontalLayout_3.addWidget(self.blueprint_tree)
        self.verticalLayout.addWidget(self.widget_2)
        BlueprintCalculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(BlueprintCalculator)
        QtCore.QMetaObject.connectSlotsByName(BlueprintCalculator)

    def retranslateUi(self, BlueprintCalculator):
        BlueprintCalculator.setWindowTitle(QtGui.QApplication.translate("BlueprintCalculator", "Blueprint Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("BlueprintCalculator", "Blueprint", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("BlueprintCalculator", "Character", None, QtGui.QApplication.UnicodeUTF8))
        self.character_combo.setItemText(0, QtGui.QApplication.translate("BlueprintCalculator", "All Level 5 Skills", None, QtGui.QApplication.UnicodeUTF8))
        self.character_combo.setItemText(1, QtGui.QApplication.translate("BlueprintCalculator", "No Skills", None, QtGui.QApplication.UnicodeUTF8))

