'''
Created on Nov 26, 2009

@author: frederikns
'''

from Model.Inventory.Type import Type
from Model.Inventory.Category import Category
from Model.Inventory.Group import Group
from Model.Inventory.MarketGroup import MarketGroup
from weakref import WeakValueDictionary

class InventoryDictionaries(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
        self.types = WeakValueDictionary()
        self.groups = WeakValueDictionary()
        self.categories = WeakValueDictionary()
        self.marketGroups = WeakValueDictionary()
        
    def get_type(self,typeID):
        if typeID not in self.types:
            type = Type(typeID)
            self.types[typeID] = type
        return self.types[typeID]
    
    def get_groups(self,groupID):
        if groupID not in self.groups:
            group = Group(groupID)
            self.groups[groupID] = group
        return self.groups[groupID]
    
    def get_category(self,categoryID):
        if categoryID not in self.categories:
            category = Category(categoryID)
            self.categories[categoryID] = category
        return self.categories[categoryID]
    
    def get_marketGroup(self,marketGroupID):
        if marketGroupID not in self.marketGroups:
            marketGroup = MarketGroup(marketGroupID)
            self.marketGroups[marketGroupID] = marketGroup
        return self.marketGroups[marketGroupID]