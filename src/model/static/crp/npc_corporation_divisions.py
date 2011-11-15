from collections import namedtuple
from model.flyweight import Flyweight
from model.static.database import database

class NPCCorporationDivision(Flyweight):
    def __init__(self,corporation_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.corporation_id = corporation_id

        cursor = database.get_cursor(
            "select * from crpNPCCorporationDivisions where corporationID={};".format(self.corporation_id))

        self.divisions = list()

        division_tuple = namedtuple("division_tuple", "division_id size ")

        for row in cursor:
            self.divisions.append(division_tuple(
                division_id=row["divisionID"],
                size=row["size"],
            ))

        cursor.close()
