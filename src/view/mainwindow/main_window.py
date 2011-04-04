from PySide import QtGui, QtCore
from view.blueprintcalculator.blueprint_calculator_view import BlueprintCalculatorView
from view.mainwindow.ui_main_window import Ui_MainWindow

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        #Initialization
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.manufacturing_calculator_button.clicked.connect(self.blueprint_calc)

    def blueprint_calc(self):
        bpc = BlueprintCalculatorView(self)
        bpc.show()
