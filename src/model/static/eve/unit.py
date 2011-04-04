from model.flyweight import Flyweight
from model.static.database import database

class Unit(Flyweight):
    def __init__(self,unit_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.unit_id = unit_id

        cursor = database.get_cursor("select * from eveUnits where \
        unitID=%s;" % (self.unit_id))
        row = cursor.fetchone()

        self.unit_name = row["unitName"]
        self.display_name = row["displayName"]
        self.description = row["description"]

        cursor.close()
