import weakref

from model.flyweight import Flyweight
from model.static.database import database

class BlueprintType(Flyweight): #IGNORE:R0902

    def __init__(self, blueprint_type_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self._blueprint_type_id = blueprint_type_id

        cursor = database.get_cursor("select * from invBlueprintTypes \
        where blueprintTypeID=%s;" % (self._blueprint_type_id))

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

        self._type = None
        self._parent_blueprint = None
        self._product_type = None
        self._material_requirements = None

    #Object reference functions
    def get_parent_blueprint_type(self):
        """Populates and returns the parent blueprint type"""
        if self._parent_blueprint is None:
            self._parent_blueprint = BlueprintType(
                    self.parent_blueprint_type_id)
        return self._parent_blueprint

    def get_type(self):
        """Populates and returns the bluprint's type"""
        if self._type is None:
            from model.static.inv.type import Type
            self._type = Type(self._blueprint_type_id)
        return self._type

    def get_product_type(self):
        """Populates and returns the blueprint's product type"""
        if self._product_type is None:
            from model.static.inv.type import Type
            self._product_type = Type(self.product_type_id)
        return self._product_type

    def get_material_requirements(self):
        """Populates and returns the blueprint's material requirements"""
        if self._material_requirements is None:
            from model.dynamic.inventory.material_requirements import \
            MaterialRequirements
            self._material_requirements = MaterialRequirements(
                self._blueprint_type_id, self.product_type_id)
        return self._material_requirements

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
        return self.get_material_requirements().get_component_blueprints()
