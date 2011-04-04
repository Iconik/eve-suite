from model.flyweight import Flyweight
from model.static.database import database

class NPCDivision(Flyweight):
    def __init__(self,division_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.division_id = division_id

        cursor = database.get_cursor("select * from crpNPCDivisions where \
        divisionID=%s;" % (self.division_id))
        row = cursor.fetchone()

        self.division_name = row["divisionName"]
        self.description = row["description"]
        self.leader_type = row["leaderType"]

        cursor.close()
