'''
Created on May 31, 2010

@author: frederikns
'''
from PySide import QtGui, QtCore
from model.static.database import database

class BlueprintCalculator(object):
    blueprint_dict = dict()
    blueprint_list = list()
    
    def __init__(self):
        self._blueprint_list_init()
        self.material_model = QtGui.QStandardItemModel()
        self.material_model.setHorizontalHeaderLabels(["Material", "Quantity",
            "Waste", "Total", "Eliminate Waste", "Next Improvement"])
        self.blueprint_model = QtGui.QStandardItemModel()
        self.blueprint_model.setHorizontalHeaderLabels(
            ["Manufacture / Blueprint", "ME", "PE"])
        self.selected_blueprint = None
        self.component_blueprints = None
        self._materials = None
        self.me_items = None
        self.pe_items = None

    def _blueprint_list_init(self):
        if len(BlueprintCalculator.blueprint_list) == 0:
            cursor = database.get_cursor("SELECT typeID, typeName FROM \
                invBlueprintTypes LEFT JOIN invTypes ON blueprintTypeID=typeID \
                WHERE published=1 ORDER BY typeName")
            for row in cursor:
                BlueprintCalculator.blueprint_dict[row["typeName"]] = row[
                    "typeID"]
                BlueprintCalculator.blueprint_list.append(row["typeName"])
            cursor.close()
            
    def blueprint_change(self,blueprint_id):
        from model.dynamic.inventory.blueprint import Blueprint
        self.me_items = list()
        self.pe_items = list()
        self.selected_blueprint = Blueprint(blueprint_id)
        self._materials = self.selected_blueprint.get_material_base()
        self.component_blueprints = list()
        
        ids = list()
        for items in self._materials:
            ids.append(items.type_id)
        query = "SELECT blueprintTypeID, productTypeID FROM invBlueprintTypes \
        WHERE productTypeID==%s " % (ids[0])
        
        for id in ids:
            if id == ids[0]:
                continue
            query += "OR productTypeID==%s " % (id)
        query += ";"
        
        cursor = database.get_cursor(query)
        #self.blueprint_model.clear()
        item = QtGui.QStandardItem(
            self.selected_blueprint.get_product_type().type_name)
        item2 = QtGui.QStandardItem("0")
        item3 = QtGui.QStandardItem("0")
        self.me_items.append(item2)
        self.pe_items.append(item3)
        #item.setCheckable(True)
        self.blueprint_model.appendRow((item,item2,item3))
        
        for row in cursor:
            blue = Blueprint(row["blueprintTypeID"])
            self.component_blueprints.append(blue)
            subitem = QtGui.QStandardItem(blue.get_product_type().type_name)
            subitem2 = QtGui.QStandardItem("0")
            subitem3 = QtGui.QStandardItem("0")
            self.me_items.append(subitem2)
            self.pe_items.append(subitem3)
            subitem.setCheckable(True)
            item.appendRow((subitem,subitem2,subitem3))
    
    def material_change(self):
        pass
    
    def time_change(self):
        pass