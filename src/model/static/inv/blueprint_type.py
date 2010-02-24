'''
Created on Dec 1, 2009

@author: frederikns
'''
from model.static.inv import inventory_dictionaries
from model.static.database import database
from model.static.inv.type_materials import TypeMaterials
from model.static.inv.type import Type
from model.static.ram.type_requirements import TypeRequirements
from model.static.ram import ram_dictionaries

class BlueprintType(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EH_HVBEREd-LgJ4IxcJkTA
    """

    def __init__(self, blueprint_type_id=None, #IGNORE:R0913
                 blueprint_type=None, blueprint_type_name=None,
                 product_type_id=None, product_type=None):
        if blueprint_type_id is not None:
            self.blueprint_type_id = blueprint_type_id
            cursor = database.get_cursor("select * from invBlueprintTypes \
            where blueprintTypeID=%s;" % (self.blueprint_type_id))
            row = cursor.fetchone()
            self.product_type_id = row["productTypeID"]
        elif blueprint_type is not None:
            self.blueprint_type_id = blueprint_type.type_id
            self.blueprint_type = blueprint_type
            cursor = database.get_cursor("select * from invBlueprintTypes \
            where blueprintTypeID=%s;" % (self.blueprint_type_id))
            row = cursor.fetchone()
            self.product_type_id = row["productTypeID"]
        elif blueprint_type_name is not None:
            cursor = database.get_cursor("select * from invTypes left join \
            invBlueprintTypes on typeID=blueprintTypeID where typeName='%s';" %
            (blueprint_type_name))
            row = cursor.fetchone()
            self.blueprint_type_id = row["blueprintTypeID"]
            self.product_type_id = row["productTypeID"]
        elif product_type_id is not None:
            self.product_type_id = product_type_id
            cursor = database.get_cursor("select * from invBlueprintTypes \
            where productTypeID=%s;" % (self.product_type_id))
            row = cursor.fetchone()
            self.blueprint_type_id = row["blueprintTypeID"]
        elif product_type is not None:
            self.product_type = product_type
            self.product_type_id = self.product_type.typeID
            cursor = database.get_cursor("select * from invBlueprintTypes \
            where productTypeID=%s;" % (self.product_type_id))
            row = cursor.fetchone()
            self.blueprint_type_id = row["blueprintTypeID"]
        
        if 'row' in locals():
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
        
        if 'cursor' in locals():
            cursor.close()
            
        self.blueprint = None
        self.parent_blueprint = None
        self.product_type = None
        self.materials = None
        self.requirements = None
        
    def get_blueprint_type(self):
        """Populates and returns the blueprint type"""
        if self.blueprint is None:
            self.blueprint_type = inventory_dictionaries.get_type(
                self.blueprint_type_id)
        return self.blueprint_type
        
    def get_parent_blueprint_type(self):
        """Populates and returns the parent blueprint type"""
        if self.parent_blueprint is None:
            self.parent_blueprint = inventory_dictionaries.get_blueprint(
                self.parent_blueprint_type_id)
        return self.parent_blueprint
        
    def get_product_type(self):
        """Populates and returns the product type"""
        if self.product_type is None:
            self.product_type = inventory_dictionaries.get_type(
                self.product_type_id)
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
    
    def get_combined(self, material_efficiency, production_efficiency_skill):
        return self.get_materials().get_combined_material_data(
            material_efficiency,
            production_efficiency_skill,
            self.waste_factor)

if __name__ == '__main__':
    def tree_print(group_names, group_relations, type_names, #IGNORE:R0913
                   type_relations, group, indent):
        """Prints a text based tree of all the tech 1 blueprints"""
        if group in group_relations:
            for rellist in group_relations[group]:
                print("%s%s" % (indent, group_names[rellist]))
                tree_print(group_names, group_relations, type_names,
                          type_relations, rellist, "%s    " % (indent))
        if group in type_relations:
            for typ_rel in type_relations[group]:
                print("%s%s" % (indent, type_names[typ_rel]))
    
    CURSOR = database.get_cursor("select marketGroupID, parentGroupID, \
    marketGroupName from invMarketGroups;")
    
    GROUP_NAMES = dict()
    GROUP_RELATIONS = dict()
    TYPE_NAMES = dict()
    TYPE_RELATIONS = dict()
    
    for ROW in CURSOR:
        GROUP_NAMES[ROW[0]] = ROW[2]
        
        if ROW[1] is not None:
            if ROW[1] not in GROUP_RELATIONS:
                GROUP_RELATIONS[ROW[1]] = list()
            GROUP_RELATIONS[ROW[1]].append(ROW[0])
    
    
    CURSOR2 = database.get_cursor("select typeID, typeName, marketGroupID \
    from invTypes INNER JOIN invBlueprintTypes ON typeID=blueprintTypeID \
    where marketGroupID<>'' AND techLevel=1;")
    
    for ROW in CURSOR2:
        TYPE_NAMES[ROW[0]] = ROW[1]
        if ROW[2] not in TYPE_RELATIONS:
            TYPE_RELATIONS[ROW[2]] = list()
        TYPE_RELATIONS[ROW[2]].append(ROW[0])
    
    tree_print(GROUP_NAMES, GROUP_RELATIONS, TYPE_NAMES, TYPE_RELATIONS, 2, "")
