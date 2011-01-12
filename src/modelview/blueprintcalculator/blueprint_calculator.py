'''
Created on May 31, 2010

@author: frederikns
'''
from model.static.database import database

class BlueprintCalculator(object):
    _blueprint_map = dict()
    _blueprint_list = list()
    
    def __init__(self):
        self._blueprint_list_init()
        self.selected_blueprint = None
        self.component_blueprints = None
        self._materials = None

    def _blueprint_list_init(self):
        if len(BlueprintCalculator._blueprint_list) == 0:
            cursor = database.get_cursor("SELECT typeID, typeName FROM \
                invBlueprintTypes LEFT JOIN invTypes ON blueprintTypeID=typeID WHERE \
                published=1 ORDER BY typeName")
            for row in cursor:
                BlueprintCalculator._blueprint_map[row["typeName"]] = row["typeID"]
                BlueprintCalculator._blueprint_list.append(row["typeName"])
            cursor.close()
            
    def blueprint_change(self,blueprint_id):
        from model.dynamic.inventory.blueprint import Blueprint
        self.selected_blueprint = Blueprint(blueprint_id)
        self._materials = self.selected_blueprint.get_material_base()
        self.component_blueprints = list()
        
        ids = list()
        for items in self._materials:
            ids.append(items.type_id)
        query = "SELECT blueprintTypeID, productTypeID FROM invBlueprintTypes WHERE productTypeID==%s " % (ids[0])
        
        for id in ids:
            if id == ids[0]:
                continue
            query += "AND productTypeID==%s " % (id)
        query += ";"
        
        cursor = database.get_cursor(query)
        
        for row in cursor:
            self.component_blueprints.append(Blueprint(row["blueprintTypeID"]))
    
    def material_change(self):
        pass
    
    def time_change(self):
        pass