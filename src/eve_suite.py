import sys
from PySide import QtGui
from view.mainwindow.main_window import MainWindow

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()

    sys.exit(app.exec_())
