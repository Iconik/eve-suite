import sys
from PyQt4 import QtGui
from View.TypeBrowser.Ui_TypeBrowser import Ui_MainWindow

class StartSkillQueueViewer(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartSkillQueueViewer()
    myapp.show()
    sys.exit(app.exec_())