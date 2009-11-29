'''
Created on Oct 28, 2009

@author: frederikns
'''
from Model.Universe import SolarSystem

from Model.Inventory import inventoryDictionaries

class Item(object):
    '''
    classdocs
    '''

    def __init__(self,id,locationID=None,quantity=None,flags=None,singleton=None):
        '''
        Constructor
        '''
        self.id = id
        self.type = inventoryDictionaries.get_type(id)
        if locationID!=None:
            self.location = SolarSystem(id)
        if quantity!=None:
            self.quantity = quantity
        if flags!=None:
            self.flags = flags
        if singleton!=None:
            self.singleton = singleton
        
    def get_id(self):
        return self.id
    def get_type(self):
        return self.type
    def get_location(self):
        return self.location
    def get_quantity(self):
        return self.quantity
    def get_flags(self):
        return self.flags
    def get_singleton(self):
        return self.singleton
    
    def get_volume(self):
        return self.quantity*self.type.get_volume()