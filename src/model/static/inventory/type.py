'''
Created on Oct 28, 2009

@author: frederikns
'''
from model.static.inventory import inventory_dictionaries
from model.static.database import database
from model.static.dgm.type_attributes import TypeAttributes

class Type(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EIEm5REREd-LgJ4IxcJkTA
    """

    def __init__(self, type_id=None, type_name=None):
        '''
        Constructor
        '''
        if type_id is not None:
            self.type_id = type_id
            cursor = database.get_cursor("select * from invTypes where \
            typeID=%s;" % (self.type_id))
            row = cursor.fetchone()
            self.type_name = row["typeName"]
        elif type_name is not None:
            self.type_name = type_name
            cursor = database.get_cursor('select * from invTypes where \
            typeName="%s";' % (self.type_name))
            row = cursor.fetchone()
            self.type_id = row["typeID"]
        
        self.group_id = row["groupID"]
        self.description = row["description"]
        self.graphic_id = row["graphicID"]
        self.radius = row["radius"]
        self.mass = row["mass"]
        self.volume = row["volume"]
        self.capacity = row["capacity"]
        self.portion_size = row["portionSize"]
        self.race_id = row["raceID"]
        self.base_price = row["basePrice"]
        self.published = row["published"]
        self.market_group_id = row["marketGroupID"]
        self.chance_of_duplicating = row["chanceOfDuplicating"]
        
        cursor.close()
        
        self.group = None
        self.market_group = None
        self.attributes = None
        
    def get_group(self):
        """Populates and returns the group"""
        if self.group is None:
            self.group = inventory_dictionaries.get_group(self.group_id)
        return self.group
    
    def get_market_group(self):
        """Populates and returns the market group"""
        if self.market_group is None:
            self.market_group = inventory_dictionaries.\
            get_market_group(self.market_group_id)
        return self.market_group
    
    def get_attributes(self):
        """Populates and returns the attributes"""
        if self.attributes is None:
            self.attributes = TypeAttributes(self.type_id)
        return self.attributes
