from model.flyweight import Flyweight
from model.static.database import database

class Config(Flyweight):
    def __init__(self,agent_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.agent_id = agent_id

        cursor = database.get_cursor("select * from agtConfig where \
        agentID=%s;" % (self.agent_id))
        
        self.location_service = False
        for row in cursor:
            if row["k"] == "level":
                self.level = row["v"]
            elif row["k"] == "quality":
                self.quality = row["v"]
            elif row["k"] == "agent.LocateCharacterService.enabled":
                self.location_service = True

        cursor.close()
