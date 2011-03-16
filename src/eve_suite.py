'''
Created on Nov 30, 2009

@author: frederikns
'''
import sys
from PySide import QtCore, QtGui
from view.blueprintcalculator.blueprint_calculator_view import BlueprintCalculatorView

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainwindow = BlueprintCalculatorView()
    mainwindow.show()
    sys.exit(app.exec_())