import sys
from PySide import QtCore, QtGui
from view.blueprintcalculator.blueprint_calculator_view import BlueprintCalculatorView
from view.mainwindow.main_window import MainWindow

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()

    sys.exit(app.exec_())
