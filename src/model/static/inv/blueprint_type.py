'''
Created on Dec 1, 2009

@author: frederikns
'''
import weakref

from model.static.database import database
from model.static.inv import inventory_dictionaries
from model.dynamic.inventory.material_requirements import MaterialRequirements


class BlueprintType(object): #IGNORE:R0902
    """
     # PyUML: Do not remove this line! # XMI_ID:_EH_HVBEREd-LgJ4IxcJkTA
    """

    def __init__(self, blueprint_type_id):
        self.blueprint_type_id = blueprint_type_id

        cursor = database.get_cursor("select * from invBlueprintTypes \
        where blueprintTypeID=%s;" % (self.blueprint_type_id))

        row = cursor.fetchone()

        self.product_type_id = row["productTypeID"]
        self.parent_blueprint_type_id = row["parentBlueprintTypeID"]
        self.production_time = row["productionTime"]
        self.tech_level = row["techLevel"]
        self.research_productivity_time = row["researchProductivityTime"]
        self.research_material_time = row["researchMaterialTime"]
        self.research_copy_time = row["researchCopyTime"]
        self.research_tech_time = row["researchTechTime"]
        self.productivity_modifier = row["productivityModifier"]
        self.material_modifier = row["materialModifier"]
        self.waste_factor = float(row["wasteFactor"])
        self.max_production_limit = row["maxProductionLimit"]

        cursor.close()

        self.blueprint = None
        self.parent_blueprint = None
        self.product_type = None
        self.material_requirements = None

    def get_parent_blueprint_type(self):
        """Populates and returns the parent blueprint type"""
        if self.parent_blueprint is None:
            self.parent_blueprint = weakref.ref(
                inventory_dictionaries.get_blueprint_type(
                    self.parent_blueprint_type_id))
        return self.parent_blueprint

    def get_product_type(self):
        """Populates and returns the product type"""
        if self.product_type is None:
            self.product_type = weakref.ref(inventory_dictionaries.get_type(
                self.product_type_id))
        return self.product_type
    
    def get_material_requirements(self):
        if self.material_requirements is None:
            self.material_requirements = MaterialRequirements(
                self.blueprint_type_id, self.product_type_id)
        return self.material_requirements

    def get_base_amounts(self):
        """Returns the base amounts for manufacturing"""
        return self.get_material_requirements().get_material_base()
    
    def get_waste(self, material_efficiency, production_efficiency_skill=5.0,
        material_multiplier=1.0):
        """Returns the waste amounts for manufacturing"""
        return self.get_material_requirements().get_material_waste(
            material_efficiency, production_efficiency_skill, self.waste_factor,
            material_multiplier)
    
    def get_totals(self, material_efficiency, production_efficiency_skill=5.0,
        material_multiplier=1.0):
        """Returns the total amounts for manufacturing"""
        return self.get_material_requirements().get_material_totals(
            material_efficiency, production_efficiency_skill, self.waste_factor,
            material_multiplier)
        
    def get_eliminate_waste(self):
        """Returns the eliminate waste levels for manufacturing"""
        return self.get_material_requirements().get_material_eliminate_waste(
            self.waste_factor)
    
    def get_next_improvement(self, material_efficiency,
        production_efficiency_skill=5.0, material_multiplier=1.0):
        """Returns the next improving level for me research"""
        return self.get_material_requirements().get_material_next_improvements(
            material_efficiency, production_efficiency_skill, self.waste_factor,
            material_multiplier)

    def get_component_blueprints(self):
        """Gets a list of blueprints required for the components"""
        pass