from PySide import QtGui, QtCore
from model.static.database import database
from collections import namedtuple

class BlueprintCalculator(object):
    blueprint_dict = dict()
    blueprint_list = list()

    def __init__(self):
        self._blueprint_list_init()

        self.material_model = QtGui.QStandardItemModel()
        self.blueprint_model = QtGui.QStandardItemModel()
        
        self.blueprint_tuple = namedtuple("blueprint_tuple", "type_id, product_type_id, blueprint, ")
        self.relation_tuple = namedtuple("relation","type_id, blueprint, \
        material_requirements, blueprintitems, ")

        self._clear_models()

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

    def _clear_models(self):
        self.material_model.clear()
        self.blueprint_model.clear()
        self.material_model.setHorizontalHeaderLabels(["Material", "Quantity",
            "Waste", "Total", "Eliminate Waste", "Next Improvement"])
        self.blueprint_model.setHorizontalHeaderLabels(
            ["Manufacture / Blueprint", "ME", "PE"])

    def populate_materials(self):
        pass

    def blueprint_change(self,blueprint_id):
        from model.dynamic.inventory.blueprint import Blueprint
        self.me_items = list()
        self.pe_items = list()
        self.selected_blueprint = Blueprint(blueprint_id)
        self._materials = self.selected_blueprint.get_material_base()
        self.component_blueprints = (
            self.selected_blueprint.get_component_blueprints())

        self._clear_models()

        item = QtGui.QStandardItem(
            self.selected_blueprint.get_product_type().type_name)
        item2 = QtGui.QStandardItem("0")
        item3 = QtGui.QStandardItem("0")
        self.me_items.append(item2)
        self.pe_items.append(item3)

        self.blueprint_model.appendRow((item,item2,item3))

        for component in self.component_blueprints:
            subitem = QtGui.QStandardItem(
                component.get_product_type().type_name)
            subitem2 = QtGui.QStandardItem("0")
            subitem3 = QtGui.QStandardItem("0")
            self.me_items.append(subitem2)
            self.pe_items.append(subitem3)
            subitem.setCheckable(True)
            subitem.setCheckState(QtCore.Qt.Checked)
            item.appendRow((subitem,subitem2,subitem3))

    def material_change(self):
        pass

    def time_change(self):
        pass
