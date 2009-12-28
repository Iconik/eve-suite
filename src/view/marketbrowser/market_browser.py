import sqlite3
from PyQt4 import QtGui

from model.static.database.database import Database

from view.marketbrowser.market_browser_template import Ui_MainWindow

class MarketBrowser(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.buildMarketTree()
        
    def buildMarketTree(self):
        '''
        Constructor
        '''
        conn = sqlite3.connect(Database.location)
        cur = conn.cursor()
        cur.execute("select marketGroupID, parentGroupID, marketGroupName from invMarketGroups")
        
        treeItems = dict()
        treeTypes = dict()
        itemRelations = dict()
        typeRelations = dict()
        
        for row in cur:
            a = QtGui.QTreeWidgetItem()
            a.setText(0, row[2])
            treeItems[row[0]] = a
            itemRelations[row[0]] = row[1]
            
        cur.execute("select typeID, typeName, marketGroupID from invTypes where marketGroupID<>'';")
        
        for row in cur:
            a = QtGui.QTreeWidgetItem()
            a.setText(0, row[1])
            treeTypes[row[0]] = a
            typeRelations[row[0]] = row[2]
        
        cur.close()
        conn.close()
        
        for key in treeItems.keys():
            if itemRelations[key] is not None:
                treeItems[itemRelations[key]].addChild(treeItems[key])
            else:
                self.ui.treeWidget.addTopLevelItem(treeItems[key])
                
        for key in treeTypes.keys():
            treeItems[typeRelations[key]].addChild(treeTypes[key])