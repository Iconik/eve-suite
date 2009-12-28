'''
Created on Nov 30, 2009

@author: frederikns
'''
from PyQt4 import QtGui
from view.mainwindow.main_window import MainWindow

import sys

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    
    mainWindow = MainWindow()
    mainWindow.show()
    
    sys.exit(app.exec_())