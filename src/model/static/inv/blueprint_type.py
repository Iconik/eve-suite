'''
Created on Dec 1, 2009

@author: frederikns
'''
import weakref

from model.static.inv import inventory_dictionaries
from model.static.database import database
from model.static.ram import ram_dictionaries


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
        self.waste_factor = row["wasteFactor"]
        self.max_production_limit = row["maxProductionLimit"]

        cursor.close()

        self.blueprint = None
        self.parent_blueprint = None
        self.product_type = None
        self.materials = None
        self.requirements = None

    def get_parent_blueprint_type(self):
        """Populates and returns the parent blueprint type"""
        if self.parent_blueprint is None:
            self.parent_blueprint = weakref.ref(
                inventory_dictionaries.get_blueprint(
                    self.parent_blueprint_type_id))
        return self.parent_blueprint

    def get_product_type(self):
        """Populates and returns the product type"""
        if self.product_type is None:
            self.product_type = weakref.ref(inventory_dictionaries.get_type(
                self.product_type_id))
        return self.product_type

    def get_materials(self):
        """Populates and returns the type materials"""
        if self.materials is None:
            self.materials = inventory_dictionaries.get_type_materials(
                self.product_type_id, self.blueprint_type_id)
        return self.materials

    def get_requirements(self):
        """Populates and returns the type requirements"""
        if self.requirements is None:
            self.requirements = ram_dictionaries.get_type_requirements(
                self.blueprint_type_id)
        return self.requirements

    def get_manufacture(self, material_efficiency, production_efficiency_skill):
        """Gets all the materials and requirements for the blueprint"""
        self.get_materials()
        self.get_requirements()