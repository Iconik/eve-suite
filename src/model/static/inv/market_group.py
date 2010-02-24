'''
Created on Nov 26, 2009

@author: frederikns
'''
from model.static.database import database
from model.static.inv import inventory_dictionaries


class MarketGroup(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EIDYyBEREd-LgJ4IxcJkTA
    """

    def __init__(self, market_group_id, parent_group_id=None, #IGNORE:R0913
                 market_group_name=None, description=None, graphics_id=None,
                 has_types=None):
        '''
        Constructor
        '''
        
        self.market_group_id = market_group_id
        
        if parent_group_id is None and market_group_name is None and \
        description is None and graphics_id is None and has_types is None:
            cursor = database.get_cursor("select * from invMarketGroups where \
            marketGroupID=%s;" % (self.market_group_id))
            row = cursor.fetchone()
        
            self.parent_group_id = row["parentGroupID"]
            self.market_group_name = row["marketGroupName"]
            self.description = row["description"]
            self.graphics_id = row["graphicsID"]
            self.has_types = row["hasTypes"]
        else:
            self.parent_group_id = parent_group_id
            self.market_group_name = market_group_name
            self.description = description
            self.graphics_id = graphics_id
            self.has_types = has_types
        
        cursor.close()
        
        self.parent_group = None
        
    def get_parent_group(self):
        """Populates and returns the parent group"""
        if self.parent_group is None:
            self.parent_group = inventory_dictionaries.\
            get_group(self.parent_group_id)
        return self.parent_group