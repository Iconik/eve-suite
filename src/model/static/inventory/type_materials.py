'''
Created on 23 Dec 2009

@author: FrederikNS
'''
from model.static.database import database
from model.dynamic.inventory.item import Item

class TypeMaterials(object):
    '''
    classdocs
    '''

    def __init__(self,type_id,waste_factor):
        '''
        Constructor
        '''
        self.type_id = type_id
        self.waste_factor = waste_factor
        self.materials = list()
        cursor = database.get_cursor("select typeID, materialTypeID, quantity \
        from invTypeMaterials where typeID=%s;" % (self.type_id))
        
        for row in cursor:
            self.materials.append(Item(row["materialTypeID"],
                                       quantity=row["quantity"]))
    
    def get_waste(self,material_efficiency=0,production_efficiency_skill=0):
        waste = list()
        for item in self.materials:
            waste.append(item.get_waste(material_efficiency, 
                                        production_efficiency_skill,
                                        self.waste_factor))
            
        return waste
            
    def get_materials(self, material_efficiency=0,
                      production_efficiency_skill=0):
        waste = self.get_waste(material_efficiency,
                               production_efficiency_skill)
        materials = list()
        for x in range(0,len(self.materials)):
            materials.append(self.materials[x].quantity+waste[x])
        
        return materials