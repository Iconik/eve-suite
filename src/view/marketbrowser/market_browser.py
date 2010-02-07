'''
Created on Oct 28, 2009

@author: frederikns
'''
from PyQt4 import QtGui

from model.static.database import database

from view.marketbrowser.market_browser_template import Ui_MainWindow

class MarketBrowser(QtGui.QMainWindow):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EIWTsBEREd-LgJ4IxcJkTA
    """
    def __init__(self, parent=None): #IGNORE:W0231
        QtGui.QWidget.__init__(self, parent) #IGNORE:W0233
        self.ui = Ui_MainWindow() #IGNORE:C0103
        self.ui.setupUi(self)
        self.buildMarketTree()
        
    def build_market_tree(self):
        """Builds a tree of the market groups"""
        cur = database.get_cursor("select marketGroupID, parentGroupID, \
        marketGroupName from invMarketGroups")
        
        tree_items = dict()
        tree_types = dict()
        item_relations = dict()
        type_relations = dict()
        
        for row in cur:
            item = QtGui.QTreeWidgetItem()
            item.setText(0, row[2])
            tree_items[row[0]] = item
            item_relations[row[0]] = row[1]
            
        cur.execute("select typeID, typeName, marketGroupID from invTypes \
        where marketGroupID<>'';")
        
        for row in cur:
            type = QtGui.QTreeWidgetItem() #IGNORE:W0622
            type.setText(0, row[1])
            tree_types[row[0]] = type
            type_relations[row[0]] = row[2]
        
        cur.close()
        
        for key in tree_items.keys():
            if item_relations[key] is not None:
                tree_items[item_relations[key]].addChild(tree_items[key])
            else:
                self.ui.treeWidget.addTopLevelItem(tree_items[key])
                
        for key in tree_types.keys():
            tree_items[type_relations[key]].addChild(tree_types[key])
