'''
Created on 23 Dec 2009

@author: FrederikNS
'''
from model.static.database import database
from model.dynamic.inventory.item import Item

class TypeMaterials(object): #IGNORE:R0903
    """
    Data-class for the materials needed for manufacturing, and returned by
    refining
    
    WARNING: The materials herein, does include the recycled materials for any
    T1 component in a T2 production.
    """
    
    def __init__(self, type_id):
        '''
        Constructor
        '''
        self.type_id = type_id
        self.materials = dict()
        cursor = database.get_cursor("select typeID, materialTypeID, quantity "
        "from invTypeMaterials where typeID=%s;" % (self.type_id))
        
        for row in cursor:
            self.materials[row["materialTypeID"]] = Item(row["materialTypeID"],
                quantity=row["quantity"])
        
    def values(self):
        return self.materials.values()
        
    def __getitem__(self, k):
        return self.materials[k]
    
    def __contains__(self, item):
        return item in self.materials