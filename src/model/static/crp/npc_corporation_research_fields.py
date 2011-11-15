from model.flyweight import Flyweight
from model.static.database import database

class NPCCorporationResearchField(Flyweight):
    def __init__(self,corporation_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.corporation_id = corporation_id

        cursor = database.get_cursor(
            "select * from crpNPCCorporationResearchFields where corporationID={};".format(self.corporation_id))

        self.skills = list()

        for row in cursor:
            self.skills.append(row["skillID"])

        cursor.close()
