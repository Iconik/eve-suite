from PyQt4 import QtGui, QtCore

from view.mainwindow.main_window_template import Ui_MainWindow
from view.skillqueueviewer.skill_queue_viewer import SkillQueueViewer
from view.blueprintcalculator.blueprint_calculator import BlueprintCalculator

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect(self.ui.CharacterViewerButton, QtCore.SIGNAL('clicked()'), self.open_skill_queue_viewer)
        self.connect(self.ui.ManufacturingCalculatorButton, QtCore.SIGNAL('clicked()'), self.open_blueprint_calculator)
        self.ui.ShipFitterButton.setEnabled(False)
        self.ui.AssetViewerButton.setEnabled(False)
        self.ui.ItemBrowserButton.setEnabled(False)
        
        
    def open_skill_queue_viewer(self):
        self.skill_queue_viewer = SkillQueueViewer()
        self.skill_queue_viewer.show()
        
    def open_blueprint_calculator(self):
        self.blueprint_calculator = BlueprintCalculator()
        self.blueprint_calculator.show()