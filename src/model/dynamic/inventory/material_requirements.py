'''
Created on Oct 13, 2010

@author: frederikns
'''
from model.static.inv import inventory_dictionaries
from model.static.ram import ram_dictionaries
import math

class MaterialRequirements(object): #IGNORE:R0902
    '''
    classdocs
    '''
    def __init__(self, blueprint_type_id=None, product_type_id=None):
        self.blueprint_type_id = blueprint_type_id
        self.product_type_id = product_type_id
        self.type_materials = inventory_dictionaries.get_type_materials(
            self.product_type_id)
        self.type_requirements = ram_dictionaries.get_type_requirements(
            self.blueprint_type_id)
        
        self.base_materials = None
        
        self.material_efficiency = None
        self.production_efficiency_skill = None
        self.waste_factor = None
        self.wastes = None
        self.eliminate_levels = None
        
    def get_reprocessing_materials(self):
        """Gets and returns the reprocessing materials for the type"""
        pass
    
    def get_material_base(self):
        """Returns the base materials, excluding recycled materials"""
        if self.base_materials is None:
            self.base_materials = list()
            for item in self.type_requirements[1]:
                if item[2] == 1: #Check if requirement is recycled
                    component = inventory_dictionaries.get_type_materials(
                        item[0].type_id)
                    for mat in self.type_materials.values():
                        if mat.type_id in component:
                            if mat.quantity > component[mat.type_id].quantity:
                                self.base_materials.append(mat-component[
                                    mat.type_id])
                        else:
                            self.base_materials.append(mat)
        return self.base_materials
        
    def get_material_waste(self, material_efficiency=0,
        production_efficiency_skill=5, waste_factor=10.0,
        material_multiplier=1.0):
        """Returns a dictionary of the waste amounts for the materials"""
        if(self.material_efficiency != material_efficiency or
            self.production_efficiency_skill != production_efficiency_skill or
            self.waste_factor != waste_factor):
            self.wastes = dict()
            for item in self.get_material_base():
                self.wastes[item.id] = waste(item.quantity, material_efficiency,
                    production_efficiency_skill, waste_factor,
                    material_multiplier)
        return self.wastes
    
    def get_material_totals(self, material_efficiency=0,
        production_efficiency_skill=5, waste_factor=10.0,
        material_multiplier=1.0):
        """Returns a dictionary of the total amounts for the materials""" 
        wastes = self.get_material_waste(material_efficiency,
            production_efficiency_skill, waste_factor, material_multiplier)
        totals = dict() 
        for item in self.get_material_base():
            totals[item.id] = item.quantity + wastes[item.id]
        return totals
    
    def get_material_eliminate_waste(self, waste_factor=10.0):
        """Returns the levels where no waste will be present for the materials
        """
        if self.eliminate_levels is None:
            self.eliminate_levels = dict()
            for item in self.get_material_base():
                self.eliminate_levels[item.id] = eliminate_waste(item.quantity,
                    waste_factor)
    
    def get_material_next_improvements(self, material_efficiency=0,
        production_efficiency_skill=5, waste_factor=10.0,
        material_multiplier=1.0):
        """Returns the next level the material would have less waste"""
        if(self.material_efficiency != material_efficiency or
            self.production_efficiency_skill != production_efficiency_skill or
            self.waste_factor != waste_factor):
            self.eliminate_levels = dict()
            for item in self.get_material_base():
                self.eliminate_levels[item.id] = (next_improvement(
                    item.quantity, material_efficiency,
                    production_efficiency_skill, waste_factor,
                    material_multiplier))
        return self.eliminate_levels

def waste(quantity, material_efficiency, production_efficiency_skill=5,
          waste_factor=10.0, material_multiplier=1.0):
    """
    Calculates manufacturing waste from parameters
    """
    return round((round(quantity * (waste_factor / 100.0) * (1.0 -
        material_efficiency) if material_efficiency <0 else (1.0 /
        (material_efficiency + 1.0)))) * (1.0 + (0.5 * (5.0 -
        production_efficiency_skill))) * material_multiplier)

def eliminate_waste(quantity, waste_factor=10.0):
    """
    Calculates the ME level required to eliminate waste
    """
    return round(0.02 * waste_factor * quantity)

def next_improvement(quantity, material_efficiency,
                     production_efficiency_skill=5, waste_factor=10.0,
                     material_multiplier=1.0):
    """
    Calculates the next ME level on which the waste improves
    """    
    return math.floor(quantity * waste_factor / ((round(quantity *
        material_multiplier * (waste_factor / ((1 - material_efficiency) if
        (material_efficiency < 0) else (1 + material_efficiency))) + (25 - 5 *
        production_efficiency_skill) / 100)) - 1) + 0.5)