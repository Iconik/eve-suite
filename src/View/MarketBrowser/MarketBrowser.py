from View.MarketBrowser.Ui_MarketBrowser import Ui_MainWindow
import sqlite3
import sys
from PyQt4 import QtGui

class StartMarketBrowser(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.buildMarketTree()
        
    def buildMarketTree(self):
        '''
        Constructor
        '''
        conn = sqlite3.connect('../../../Resources/Database/apo15-sqlite3-v1.db')
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
        
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartMarketBrowser()
    myapp.show()
    sys.exit(app.exec_())