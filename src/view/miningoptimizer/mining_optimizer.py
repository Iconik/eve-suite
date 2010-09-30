'''
Created on Jan 31, 2010

@author: frederikns
'''
from PyQt4 import QtGui
from view.miningoptimizer.mining_optimizer_template import \
Ui_mining_optimizer_window

class MiningOptimizer(QtGui.QMainWindow):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EIW6yREREd-LgJ4IxcJkTA
    """

    def __init__(self, parent=None): #IGNORE:W0231
        QtGui.QWidget.__init__(self, parent) #IGNORE:W0233
        self.ui = Ui_mining_optimizer_window() #IGNORE:C0103
        self.ui.setupUi(self)
        for col in range(0, self.ui.mineral_tree.columnCount()):
            self.ui.mineral_tree.resizeColumnToContents(col)
        for col in range(0, self.ui.mine_tree.columnCount()):
            self.ui.mine_tree.resizeColumnToContents(col)
            
    