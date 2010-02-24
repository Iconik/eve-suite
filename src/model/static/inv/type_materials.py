'''
Created on 23 Dec 2009

@author: FrederikNS
'''
from model.static.database import database
from model.dynamic.inventory.item import Item
from model.static.inv import inventory_dictionaries
import math

class TypeMaterials(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EIHDIBEREd-LgJ4IxcJkTA
    """

    def __init__(self, type_id, blueprint_type_id=None):
        '''
        Constructor
        '''
        self.type_id = type_id
        self.blueprint_type_id = blueprint_type_id
        self.materials = list()
        cursor = database.get_cursor("select typeID, materialTypeID, quantity \
        from invTypeMaterials where typeID=%s;" % (self.type_id))
        
        for row in cursor:
            self.materials.append(Item(row["materialTypeID"],
                                       quantity=row["quantity"]))
        self.manufacturing_materials = None
            
        
        
    def get_manufacturing_materials(self):
        """Calculates the actual materials needed for manufacturing (excluding
        reprocessing materials) and returns them"""
        if self.manufacturing_materials is None:
            self.manufacturing_materials = list()
            blueprint = inventory_dictionaries.get_blueprint(
                self.blueprint_type_id)
            requirements = blueprint.get_requirements().requirements[1]
            recycled = list()
            for item in requirements:
                if item[2] == 1: #is recycled
                    recycled = inventory_dictionaries.get_type_materials(
                        item[0].type_id).materials
            for item2 in self.materials:
                found = False
                for item3 in recycled:
                    if item2.type_id == item3.type_id:
                        found = True
                        if item2.quantity > item3.quantity:
                            self.manufacturing_materials.append(Item(
                                item2.type_id,
                                quantity=item2.quantity-item3.quantity))
                if found == False:
                    self.manufacturing_materials.append(Item(item2.type_id,
                        quantity=item2.quantity))
        return self.manufacturing_materials
    
    def get_combined_material_data(self, material_efficiency,
                                   production_efficiency_skill, waste_factor):
        """Calculates and combines the base quantity, waste, total, next
        improvement, and perfect me into one list, and returns it"""
        combined = list()
        for item in self.get_manufacturing_materials():
            waste_amount = waste(item.quantity,
                                 material_efficiency,
                                 production_efficiency_skill,
                                 waste_factor)
            total_amount = item.quantity + waste_amount
            combined.append((item,
                             waste_amount,
                             total_amount,
                             next_improvement(),
                             eliminate_waste(item.quantity, waste_factor)))
        return combined

def waste(quantity, material_efficiency, production_efficiency_skill=5.0,
          waste_factor=10.0):
    """Calculates waste from parameters"""
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
    """Calculates the ME level required to eliminate waste"""
    return math.ceil(0.2 * waste_factor * quantity)

def next_improvement():
    """Calculates the next ME level on which the waste improves"""
    return 0