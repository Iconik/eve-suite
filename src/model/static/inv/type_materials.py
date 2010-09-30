'''
Created on 23 Dec 2009

@author: FrederikNS
'''
from model.static.database import database
from model.dynamic.inventory.item import Item

class TypeMaterials(object):
    """
    Class for the materials needed for manufacturing, and returned by refining
    """
    def __init__(self, type_id):
        '''
        Constructor
        '''
        self.type_id = type_id
        self.materials = list()
        cursor = database.get_cursor("select typeID, materialTypeID, quantity \
        from invTypeMaterials where typeID=%s;" % (self.type_id))
        
        for row in cursor:
            self.materials.append(Item(row["materialTypeID"],
                                       quantity=row["quantity"]))
        self.manufacturing_materials = None
        
    def get_manufacturing_materials(self, material_efficiency,
                                    production_efficiency_skill=5.0,
                                    waste_factor=10.0):
        """
        Returns list of materials, along with corresponding wastes, optimal
        levels and the next improving level.
        """
        materials = list()
        for material in self.materials:
            materials.append((material,
                              waste(material.quantity,
                                    material_efficiency,
                                    production_efficiency_skill),
                              eliminate_waste(material.quantity, waste_factor),
                              next_improvement()))
        return materials
    
    
        

def waste(quantity, material_efficiency, production_efficiency_skill=5.0,
          waste_factor=10.0):
    """
    Calculates waste from parameters
    """
    if material_efficiency >= 0:
        return round((round(quantity *
                            (waste_factor / 100.0) *
                            (1.0 / (material_efficiency + 1.0)))) *
                     (1.0 + (0.5 * (5.0 - production_efficiency_skill))))
    else:
        return round((round(quantity *
                            (waste_factor / 100.0) *
                            (1.0 - material_efficiency))) *
                     (1.0 + (0.5 * (5.0 - production_efficiency_skill))))

def eliminate_waste(quantity, waste_factor=10.0):
    """
    Calculates the ME level required to eliminate waste
    """
    return round(0.02 * waste_factor * quantity)

def next_improvement():
    """
    Calculates the next ME level on which the waste improves
    """
    return 0