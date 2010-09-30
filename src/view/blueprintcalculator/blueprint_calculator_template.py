# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blueprint_calculator_template.ui'
#
# Created: Wed Feb 24 23:40:48 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 393)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.blueprint_label = QtGui.QLabel(self.groupBox)
        self.blueprint_label.setObjectName("blueprint_label")
        self.horizontalLayout_2.addWidget(self.blueprint_label)
        self.blueprint_combo = QtGui.QComboBox(self.groupBox)
        self.blueprint_combo.setEditable(True)
        self.blueprint_combo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.blueprint_combo.setMinimumContentsLength(47)
        self.blueprint_combo.setObjectName("blueprint_combo")
        self.horizontalLayout_2.addWidget(self.blueprint_combo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.me_label = QtGui.QLabel(self.groupBox)
        self.me_label.setObjectName("me_label")
        self.horizontalLayout_3.addWidget(self.me_label)
        self.me_spin = QtGui.QSpinBox(self.groupBox)
        self.me_spin.setMinimum(-2147483647)
        self.me_spin.setMaximum(2147483647)
        self.me_spin.setObjectName("me_spin")
        self.horizontalLayout_3.addWidget(self.me_spin)
        self.pe_label = QtGui.QLabel(self.groupBox)
        self.pe_label.setObjectName("pe_label")
        self.horizontalLayout_3.addWidget(self.pe_label)
        self.pe_spin = QtGui.QSpinBox(self.groupBox)
        self.pe_spin.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.pe_spin.setMinimum(-2147483647)
        self.pe_spin.setMaximum(2147483647)
        self.pe_spin.setObjectName("pe_spin")
        self.horizontalLayout_3.addWidget(self.pe_spin)
        self.runs_label = QtGui.QLabel(self.groupBox)
        self.runs_label.setObjectName("runs_label")
        self.horizontalLayout_3.addWidget(self.runs_label)
        self.runs_spin = QtGui.QSpinBox(self.groupBox)
        self.runs_spin.setMinimum(1)
        self.runs_spin.setMaximum(2147483647)
        self.runs_spin.setObjectName("runs_spin")
        self.horizontalLayout_3.addWidget(self.runs_spin)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pe_skill_combo = QtGui.QComboBox(self.groupBox_2)
        self.pe_skill_combo.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.pe_skill_combo.setObjectName("pe_skill_combo")
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.material_table = QtGui.QTreeWidget(self.centralwidget)
        self.material_table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.material_table.setObjectName("material_table")
        self.verticalLayout_2.addWidget(self.material_table)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Blueprint Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.blueprint_label.setText(QtGui.QApplication.translate("MainWindow", "Blueprint:", None, QtGui.QApplication.UnicodeUTF8))
        self.me_label.setText(QtGui.QApplication.translate("MainWindow", "ME:", None, QtGui.QApplication.UnicodeUTF8))
        self.pe_label.setText(QtGui.QApplication.translate("MainWindow", "PE:", None, QtGui.QApplication.UnicodeUTF8))
        self.runs_label.setText(QtGui.QApplication.translate("MainWindow", "Runs:", None, QtGui.QApplication.UnicodeUTF8))
        self.material_table.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.material_table.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Base Amount", None, QtGui.QApplication.UnicodeUTF8))
        self.material_table.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Waste Amount", None, QtGui.QApplication.UnicodeUTF8))
        self.material_table.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Total Amount", None, QtGui.QApplication.UnicodeUTF8))
        self.material_table.headerItem().setText(4, QtGui.QApplication.translate("MainWindow", "Unit Price", None, QtGui.QApplication.UnicodeUTF8))
        self.material_table.headerItem().setText(5, QtGui.QApplication.translate("MainWindow", "Total Price", None, QtGui.QApplication.UnicodeUTF8))
        self.material_table.headerItem().setText(6, QtGui.QApplication.translate("MainWindow", "Improve At Level", None, QtGui.QApplication.UnicodeUTF8))
        self.material_table.headerItem().setText(7, QtGui.QApplication.translate("MainWindow", "Perfect ME", None, QtGui.QApplication.UnicodeUTF8))

