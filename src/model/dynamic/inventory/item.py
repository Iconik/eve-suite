'''
Created on Oct 28, 2009

@author: frederikns
'''

from model.static.inventory import inventory_dictionaries
from model.static.map import map_dictionaries
import math

class Item(object):
    '''
    classdocs
    '''

    def __init__(self, type_id, locationID=None, quantity=None, flags=None,
                 singleton=None):
        '''
        Constructor
        '''
        self.type_id = type_id
        if locationID is not None:
            self.location_id = id
        if quantity is not None:
            self.quantity = quantity
        if flags is not None:
            self.flags = flags
        if singleton is not None:
            self.singleton = singleton
    
    def get_type(self):
        if 'self.type' not in locals():
            self.type = inventory_dictionaries.get_type(self.type_id)
        return self.type
    
    def get_location(self):
        if 'self.location' not in locals():
            self.location = map_dictionaries.get_solar_system(self.location_id)
        return self.location
    
    def get_volume(self):
        return self.quantity*self.type.get_volume()
    
    """ Calculates the amount of waste in manufacturing
    
    This is only used when the item is part of a blueprint's type_materials
    """
    def get_waste(self, material_efficiency=0, production_efficiency_skill=0,
                  waste_factor=0.10):
        if material_efficiency >= 0:
            return int(round(float(self.quantity) *
                             ((float(waste_factor) / 100) *
                              (1 / float(material_efficiency + 1)) +
                              (5 - production_efficiency_skill) * 0.05)))
        if material_efficiency < 0:
            return int(round(float(self.quantity) *
                             ((float(waste_factor) / 100) *
                              (1 - material_efficiency) +
                              (5 - production_efficiency_skill) * 0.05)))
        
    def get_perfect_me(self,waste_factor=0.10):
        return int(math.ceil(0.02*waste_factor*self.quantity))