'''
Created on Mar 20, 2011

@author: frederikns
'''
from model.flyweight import Flyweight
from collections import namedtuple
from model.static.database import database
from model.dynamic.inventory.item import Item

class SchematicTypeMap(Flyweight):
    def __init__(self,schematic_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.schematic_id = schematic_id

        cursor = database.get_cursor(
            "select * from planetSchematicTypeMap where schematicID={};".format(self.schematic_id))

        types = list()

        schematic_type = namedtuple("schematic_type", "item, is_input")

        for row in cursor:
            types.append(schematic_type(
                item=Item(row["typeID"], row["quantity"]),
                is_input=(row["isInput"])))

        cursor.close()
