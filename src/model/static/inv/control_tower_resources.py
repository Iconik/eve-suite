from collections import namedtuple
from model.flyweight import Flyweight
from model.static.database import database

class ControlTowerResource(Flyweight):
    def __init__(self,control_tower_type_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.control_tower_type_id = control_tower_type_id

        cursor = database.get_cursor("select * from invControlTowerResources where \
        controlTowerTypeID=%s;" % (self.control_tower_type_id))

        self.resources = list()

        resource_tuple = namedtuple("resource_tuple",
            "resource_type_id purpose quantity min_security_level faction_id ")

        for row in cursor:
            self.resources.append(resource_tuple(
                resource_type_id=row["resourceTypeID"],
                purpose=row["purpose"],
                quantity=row["quantity"],
                min_security_level=row["minSecurityLevel"],
                faction_id=row["factionID"]))

        cursor.close()
