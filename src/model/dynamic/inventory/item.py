'''
Created on Oct 28, 2009

@author: frederikns
'''

from model.static.inventory import inventory_dictionaries
from model.static.map import map_dictionaries

class Item(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_hdn2ghEPEd-LgJ4IxcJkTA
    """

    def __init__(self, type_id, location_id=None, quantity=None, #IGNORE:R0913
                 flags=None, singleton=None):
        self.type_id = type_id
        if location_id is not None:
            self.location_id = id
        if quantity is not None:
            self.quantity = quantity
        if flags is not None:
            self.flags = flags
        if singleton is not None:
            self.singleton = singleton
            
        self.type = None
        self.location = None
    
    def get_type(self):
        """Populates the type and returns it"""
        if self.type is None:
            self.type = inventory_dictionaries.get_type(self.type_id)
        return self.type
    
    def get_location(self):
        """Populates the location and returns it"""
        if self.location is None:
            self.location = map_dictionaries.get_solar_system(self.location_id)
        return self.location
    
    def get_volume(self):
        """Returns the volume of the item"""
        return self.quantity*self.type.get_volume()
