'''
Created on Oct 28, 2009

@author: frederikns
'''
from PyQt4 import QtGui, QtCore

from view.mainwindow.main_window_template import Ui_MainWindow
from view.skillqueueviewer.skill_queue_viewer import SkillQueueViewer
from view.blueprintcalculator.blueprint_calculator import BlueprintCalculator
from view.miningoptimizer.mining_optimizer import MiningOptimizer

class MainWindow(QtGui.QMainWindow):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EIUehxEREd-LgJ4IxcJkTA
    """
    def __init__(self, parent=None): #IGNORE:W0231
        QtGui.QWidget.__init__(self, parent) #IGNORE:W0233
        self.ui = Ui_MainWindow() #IGNORE:C0103
        self.ui.setupUi(self)
        self.connect(self.ui.CharacterViewerButton, QtCore.SIGNAL('clicked()'),
                     self.open_skill_queue_viewer)
        self.connect(self.ui.ManufacturingCalculatorButton,
                     QtCore.SIGNAL('clicked()'),
                     self.open_blueprint_calculator)
        self.connect(self.ui.MiningCalculatorButton,
                     QtCore.SIGNAL('clicked()'),
                     self.open_mining_calculator)
        self.ui.ShipFitterButton.setEnabled(False)
        self.ui.AssetViewerButton.setEnabled(False)
        self.ui.ItemBrowserButton.setEnabled(False)
        self.ui.RefineCalculatorButton.setEnabled(False)
        self.ui.ResearchCalculatorButton.setEnabled(False)
        self.ui.POSFitterButton.setEnabled(False)
        self.ui.SkillBrowserButton.setEnabled(False)
        self.ui.SkillPlannerButton.setEnabled(False)
        self.ui.TravelPlannerButton.setEnabled(False)
        
        self.skill_queue_viewer = None
        self.blueprint_calculator = None
        self.mining_calculator = None
        
    def open_skill_queue_viewer(self):
        """Opens the skill queue viewer window"""
        if self.skill_queue_viewer is None:
            self.skill_queue_viewer = SkillQueueViewer()
        self.skill_queue_viewer.show()
        
    def open_blueprint_calculator(self):
        """Opens the blueprint calculator window"""
        if self.blueprint_calculator is None:
            self.blueprint_calculator = BlueprintCalculator()
        self.blueprint_calculator.show()
        
    def open_mining_calculator(self):
        """Opens the mining calculator window"""
        if self.mining_calculator is None:
            self.mining_calculator = MiningOptimizer()
        self.mining_calculator.show()
