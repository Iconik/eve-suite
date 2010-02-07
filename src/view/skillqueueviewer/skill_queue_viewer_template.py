# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Skill Queue Viewer.ui'
#
# Created: Mon Nov 23 14:16:22 2009
#      by: PyQt4 UI code generator 4.6.2-snapshot-20091118
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EIYv8xEREd-LgJ4IxcJkTA
    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 581)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_userID = QtGui.QLabel(self.centralwidget)
        self.label_userID.setObjectName("label_userID")
        self.gridLayout.addWidget(self.label_userID, 0, 0, 1, 1)
        self.label_apiKey = QtGui.QLabel(self.centralwidget)
        self.label_apiKey.setObjectName("label_apiKey")
        self.gridLayout.addWidget(self.label_apiKey, 1, 0, 1, 1)
        self.label_character = QtGui.QLabel(self.centralwidget)
        self.label_character.setObjectName("label_character")
        self.gridLayout.addWidget(self.label_character, 2, 0, 1, 1)
        self.text_userID = QtGui.QLineEdit(self.centralwidget)
        self.text_userID.setObjectName("text_userID")
        self.gridLayout.addWidget(self.text_userID, 0, 1, 1, 1)
        self.text_apiKey = QtGui.QLineEdit(self.centralwidget)
        self.text_apiKey.setObjectName("text_apiKey")
        self.gridLayout.addWidget(self.text_apiKey, 1, 1, 1, 1)
        self.combo_character = QtGui.QComboBox(self.centralwidget)
        self.combo_character.setObjectName("combo_character")
        self.gridLayout.addWidget(self.combo_character, 2, 1, 1, 1)
        self.button_fetchCharacters = QtGui.QPushButton(self.centralwidget)
        self.button_fetchCharacters.setObjectName("button_fetchCharacters")
        self.gridLayout.addWidget(self.button_fetchCharacters, 3, 0, 1, 1)
        self.button_fetchQueue = QtGui.QPushButton(self.centralwidget)
        self.button_fetchQueue.setObjectName("button_fetchQueue")
        self.gridLayout.addWidget(self.button_fetchQueue, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tree_skill = QtGui.QTreeWidget(self.centralwidget)
        self.tree_skill.setColumnCount(3)
        self.tree_skill.setObjectName("tree_skill")
        self.verticalLayout.addWidget(self.tree_skill)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.text_userID, self.text_apiKey)
        MainWindow.setTabOrder(self.text_apiKey, self.combo_character)
        MainWindow.setTabOrder(self.combo_character, self.button_fetchCharacters)
        MainWindow.setTabOrder(self.button_fetchCharacters, self.button_fetchQueue)
        MainWindow.setTabOrder(self.button_fetchQueue, self.tree_skill)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Skill Queue Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_userID.setText(QtGui.QApplication.translate("MainWindow", "UserID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_apiKey.setText(QtGui.QApplication.translate("MainWindow", "API Key", None, QtGui.QApplication.UnicodeUTF8))
        self.label_character.setText(QtGui.QApplication.translate("MainWindow", "Character", None, QtGui.QApplication.UnicodeUTF8))
        self.button_fetchCharacters.setText(QtGui.QApplication.translate("MainWindow", "Fetch Characters", None, QtGui.QApplication.UnicodeUTF8))
        self.button_fetchQueue.setText(QtGui.QApplication.translate("MainWindow", "Fetch Skill Queue", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_skill.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_skill.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Start Date", None, QtGui.QApplication.UnicodeUTF8))
        self.tree_skill.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "End Date", None, QtGui.QApplication.UnicodeUTF8))

