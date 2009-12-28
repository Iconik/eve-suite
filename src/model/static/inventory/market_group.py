'''
Created on Nov 26, 2009

@author: frederikns
'''
from model.static.database import database
from model.static.inventory import inventory_dictionaries


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
            cursor = database.get_cursor("select * from invMarketGroups where marketGroupID=%s;" % (self.marketGroupID))
            row = cursor.fetchone()
        
            self.parentGroupID = row["parentGroupID"]
            self.marketGroupName = row["marketGroupName"]
            self.description = row["description"]
            self.graphicsID = row["graphicsID"]
            self.hasTypes = row["hasTypes"]
        else:
            self.parentGroupID = parentGroupID
            self.marketGroupName = marketGroupName
            self.description = description
            self.graphicsID = graphicsID
            self.hasTypes = hasTypes
        
        cursor.close()
        
    def get_parent_group(self):
        if 'self.parent_group' not in locals():
            self.parent_group = inventory_dictionaries.get_group(self.parentGroupID)
        return self.parent_group