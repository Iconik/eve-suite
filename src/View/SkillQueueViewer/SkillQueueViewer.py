from time import localtime
from datetime import datetime
from calendar import timegm

import sys
from PyQt4 import QtCore, QtGui
from View.SkillQueueViewer.Ui_SkillQueueViewer import Ui_MainWindow
from Model.Account.Account import Account

class StartSkillQueueViewer(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tree_skill.setColumnWidth(0, 200)
        self.ui.tree_skill.setColumnWidth(1, 200)
        self.ui.tree_skill.setColumnWidth(2, 200)
        
        QtCore.QObject.connect(self.ui.button_fetchCharacters, QtCore.SIGNAL("clicked()"), self.fetchCharacters)
        QtCore.QObject.connect(self.ui.button_fetchQueue, QtCore.SIGNAL("clicked()"), self.fetchSkillQueue)
        
    def fetchCharacters(self):
        self.ui.combo_character.clear()
        self.account = Account(self.ui.text_userID.text(), self.ui.text_apiKey.text())
        for char in self.account.get_characters():
            self.ui.combo_character.addItem(char.get_name())
            
    def fetchSkillQueue(self):
        self.ui.tree_skill.clear()
        for char in self.account.get_characters():
            if char.get_name() == self.ui.combo_character.currentText():
                for skill in char.get_skill_queue():
                    a = QtGui.QTreeWidgetItem(self.ui.tree_skill)
                    a.setText(0, "%s %s" % (skill.get_name(), skill.get_level()))
                    a.setText(1, datetime(*localtime(timegm(skill.get_startTime().timetuple()))[0:6]).isoformat(" "))
                    a.setText(2, datetime(*localtime(timegm(skill.get_endTime().timetuple()))[0:6]).isoformat(" "))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartSkillQueueViewer()
    myapp.show()
    sys.exit(app.exec_())