import sys
from time import localtime
from datetime import datetime
from calendar import timegm
from PyQt4 import QtCore, QtGui

from model.dynamic.account.account import Account

from view.skillqueueviewer.skill_queue_viewer_template import Ui_MainWindow

class SkillQueueViewer(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tree_skill.setColumnWidth(0, 200)
        self.ui.tree_skill.setColumnWidth(1, 200)
        self.ui.tree_skill.setColumnWidth(2, 200)
        
        QtCore.QObject.connect(self.ui.button_fetchCharacters, QtCore.SIGNAL("clicked()"), self.fetch_characters)
        QtCore.QObject.connect(self.ui.button_fetchQueue, QtCore.SIGNAL("clicked()"), self.fetch_skill_queue)
        
    def fetch_characters(self):
        self.ui.combo_character.clear()
        self.account = Account(str(self.ui.text_userID.text()), str(self.ui.text_apiKey.text()))
        for char in self.account.get_characters():
            self.ui.combo_character.addItem(char.get_name())
            
    def fetch_skill_queue(self):
        self.ui.tree_skill.clear()
        for char in self.account.get_characters():
            if char.get_name() == self.ui.combo_character.currentText():
                for skill in char.get_skill_queue():
                    a = QtGui.QTreeWidgetItem(self.ui.tree_skill)
                    a.setText(0, "%s %s" % (skill.get_name(), skill.get_level()))
                    a.setText(1, datetime(*localtime(timegm(skill.get_startTime().timetuple()))[0:6]).isoformat(" "))
                    a.setText(2, datetime(*localtime(timegm(skill.get_endTime().timetuple()))[0:6]).isoformat(" "))