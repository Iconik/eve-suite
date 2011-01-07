'''
Created on May 31, 2010

@author: frederikns
'''
from model.static.database import database
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
        self.materials = self.selected_blueprint.get_base_amounts()
        
        ids = list()
        for items in self.materials:
            ids.append(items.type_id)
        query = "SELECT blueprintTypeID, productTypeID FROM invBlueprintTypes WHERE pruductTypeID==%s " % (ids[0])
        
        for id in ids:
            if id[0] == ids[0][0] and id[1] == ids[0][1]:
                continue
            query += "AND productTypeID==%s " % (id)
        
        query += ";"
        
            
    
    def material_change(self):
        pass
    
    def time_change(self):
        pass