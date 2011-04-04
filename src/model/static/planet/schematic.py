'''
Created on Mar 20, 2011

@author: frederikns
'''
from model.flyweight import Flyweight
from model.static.database import database

class Schematic(Flyweight):
    def __init__(self,schematic_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.schematic_id = schematic_id

        cursor = database.get_cursor("select * from planetSchematics where \
        schematicID=%s;" % (self.schematic_id))
        row = cursor.fetchone()

        self.schematic_name = row["schematicName"]
        self.cycle_time = row["cycleTime"]

        cursor.close()
