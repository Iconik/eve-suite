'''
Created on May 31, 2010

@author: frederikns
'''
from model.static.database import database
from model.static.inv.type_materials import TypeMaterials
from model.dynamic.inventory.blueprint import Blueprint

class BlueprintCalculator(object):
    def __init__(self):
        self.blueprint_map = dict()
        self.blueprint_list = list()
        self._blueprint_list_init()
        self.selected_blueprint = None
        self.materials = dict()

    def _blueprint_list_init(self):
        cursor = database.get_cursor("SELECT typeID, typeName FROM \
            invBlueprintTypes LEFT JOIN invTypes ON blueprintTypeID=typeID WHERE \
            published=1 ORDER BY typeName")
        for row in cursor:
            self.blueprint_map[row["typeName"]] = row["typeID"]
            self.blueprint_list.append(row["typeName"])
        cursor.close()
            
    def blueprint_change(self,blueprint_id):
        self.selected_blueprint = Blueprint(blueprint_id)
        self.materials = self.selected_blueprint.get_combined(production_efficiency_skill)
    
    def material_change(self):
        pass
    
    def time_change(self):
        pass