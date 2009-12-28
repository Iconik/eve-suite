'''
Created on Dec 1, 2009

@author: frederikns
'''
from model.static.inventory import inventory_dictionaries
from model.static.database import database
from model.static.inventory.type_materials import TypeMaterials
from model.static.inventory.type import Type

class BlueprintType(object):
    '''
    classdocs
    '''

    def __init__(self, blueprint_type_id=None, blueprint_type=None,
                 blueprint_type_name=None, product_type_id=None,
                 product_type=None):
        '''
        Constructor
        '''
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
        
        if 'cursor' in locals:
            cursor.close()
        
    def get_blueprint_type(self):
        if 'self.blueprint' not in locals():
            self.blueprint_type = Type(self.blueprint_type_id)
        return self.blueprint_type
        
    def get_parent_blueprint_type(self):
        if 'self.parent_blueprint' not in locals():
            self.parent_blueprint = inventory_dictionaries.get_blueprint(
                                                self.parent_blueprint_type_id)
        return self.parent_blueprint
        
    def get_product_type(self):
        if 'self.product_type' not in locals():
            self.product_type = inventory_dictionaries.get_type(
                                                        self.product_type_id)
        return self.product_type
    
    def get_build_materials(self):
        if 'self.build_materials' not in locals():
            self.build_materials = TypeMaterials(self.product_type_id,
                                                 self.waste_factor)
        return self.build_materials
    
    def get_materials(self):
        return self.get_build_materials()

if __name__ == '__main__':
    def treePrint(groupNames, groupRelations, typeNames, typeRelations, group,
                  indent):
        if group in groupRelations:
            for rellist in groupRelations[group]:
                print("%s%s" % (indent, groupNames[rellist]))
                treePrint(groupNames, groupRelations, typeNames, typeRelations,
                          rellist, "%s    " % (indent))
        if group in typeRelations:
            for x in typeRelations[group]:
                print("%s%s" % (indent, typeNames[x]))
        pass
    
    cursor = database.get_cursor("select marketGroupID, parentGroupID, \
    marketGroupName from invMarketGroups;")
    
    groupNames = dict()
    groupRelations = dict()
    typeNames = dict()
    typeRelations = dict()
    
    for row in cursor:
        groupNames[row[0]] = row[2]
        
        if row[1] is not None:
            if row[1] not in groupRelations:
                groupRelations[row[1]] = list()
            groupRelations[row[1]].append(row[0])
    
    
    cursor2 = database.get_cursor("select typeID, typeName, marketGroupID \
    from invTypes INNER JOIN invBlueprintTypes ON typeID=blueprintTypeID \
    where marketGroupID<>'' AND techLevel=1;")
    
    for row in cursor2:
        typeNames[row[0]] = row[1]
        if row[2] not in typeRelations:
            typeRelations[row[2]] = list()
        typeRelations[row[2]].append(row[0])
    
    treePrint(groupNames,groupRelations,typeNames,typeRelations,2,"")
    
    pass