'''
Created on Nov 26, 2009

@author: frederikns
'''
import sqlite3

class MarketGroup(object):
    '''
    classdocs
    '''


    def __init__(self,marketGroupID,parentGroupID=None,marketGroupName=None,description=None,graphicsID=None,hasTypes=None):
        '''
        Constructor
        '''
        
        self.marketGroupID = marketGroupID
        
        if parentGroupID is None and marketGroupName is None and description is None and graphicsID is None and hasTypes is None:
            conn = sqlite3.connect('../../../Resources/Database/apo15-sqlite3-v1.db')
            cur = conn.cursor()
            cur.execute("select * from invMarketGroups where marketGroupID='%s';" % (self.marketGroupID))
            row = cur.fetchone()
        
            self.parentGroupID = row[1]
            self.marketGroupName = row[2]
            self.description = row[3]
            self.graphicsID = row[4]
            self.hasTypes = row[5]
        else:
            self.parentGroupID = parentGroupID
            self.marketGroupName = marketGroupName
            self.description = description
            self.graphicsID = graphicsID
            self.hasTypes = hasTypes
        
        cur.close()
        conn.close()
        
    def getParentID(self):
        return self.parentGroupID
    
    def getMarketGroupName(self):
        return self.marketGroupName