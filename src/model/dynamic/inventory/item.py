'''
Created on Oct 28, 2009

@author: frederikns
'''

from model.static.inv import inventory_dictionaries
from model.static.map import map_dictionaries
from copy import copy

class Item(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_hdn2ghEPEd-LgJ4IxcJkTA
    """

    def __init__(self, type_id=None, location_id=None, quantity=None,
                 flags=None, singleton=None):
        
        self.type_id = type_id    
        self.location_id = location_id
        self.quantity = quantity
        self.flags = flags
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
        return self.quantity*self.get_type().volume
    
    def __add__(self, other):
        item = copy(self)
        if isinstance(other, Item):
            if self.type_id == other.type_id:
                item.quantity += other.quantity
                return item
        else:
            item.quantity += other
            return item
        
    def __sub__(self, other):
        item = copy(self)
        if isinstance(other, Item):
            if self.type_id == other.type_id:
                item.quantity -= other.quantity
                return item
        else:
            item.quantity -= other
            return item
        
    def __mul__(self, other):
        item = copy(self)
        item.quantity *= other
        return item
    
    def __div__(self, other):
        item = copy(self)
        item.quantity /= other
        return item