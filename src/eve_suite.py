'''
Created on Nov 30, 2009

@author: frederikns
'''
from PyQt4 import QtGui
from view.mainwindow.main_window import MainWindow
from model.static.inv import inventory_dictionaries

import sys

if __name__ == '__main__':
    APP = QtGui.QApplication(sys.argv)
    
    MAIN_WINDOW = MainWindow()
    MAIN_WINDOW.show()
    
    sys.exit(APP.exec_())