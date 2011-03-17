'''
Created on Oct 28, 2009

@author: frederikns
'''
from copy import copy

class Item(object):
    def __init__(self, type_id=None, location_id=None, quantity=None,
        flags=None, singleton=None):
        self.type_id = type_id
        self.location_id = location_id
        self.quantity = quantity
        self.flags = flags
        self.singleton = singleton
        
        self._type = None    
        self._location = None
    
    def get_type(self):
        """Populates the _type and returns it"""
        if self._type is None:
            from model.static.inv.type import Type
            self._type = Type(self.type_id)
        return self._type
    
    def get_blueprint_type(self):
        return self.get_type().get_blueprint_type()
    
    def get_location(self):
        """Populates the _location and returns it"""
        if self._location is None:
            from model.static.map.solar_system import SolarSystem
            self._location = SolarSystem(self.location_id)
        return self._location
    
    def get_volume(self):
        """Returns the volume of the item"""
        return self.quantity*self.get_type().volume
    
    def copy(self):
        return copy(self)
    
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
        """Divides an item amount by another item amount"""
        item = copy(self)
        item.quantity /= other
        return item
    
def get_volume(items):
    """Takes a list of items or an item and returns the total volume"""
    if isinstance(items, Item):
        return items.get_volume()
    if isinstance(items, list()):
        total_vol = 0 
        for x in items:
            total_vol += x.get_volume()
        return total_vol