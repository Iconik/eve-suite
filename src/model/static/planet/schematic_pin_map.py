'''
Created on Mar 20, 2011

@author: frederikns
'''
from model.flyweight import Flyweight
from model.static.database import database

class SchematicPinMap(Flyweight):
    def __init__(self,schematic_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.schematic_id = schematic_id

        cursor = database.get_cursor(
            "select * from planetSchematicPinMap where schematicID={}".format(
                self.schematic_id))

        self.pin_type_ids = list()

        for row in cursor:
            self.pin_type_ids.append(row["pinTypeID"])

        cursor.close()
