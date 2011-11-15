from model.flyweight import Flyweight
from model.static.database import database

class Agent(Flyweight):
    def __init__(self,agent_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.agent_id = agent_id

        cursor = database.get_cursor(
            "select * from agtAgents where agentID={};".format(self.agent_id))
        row = cursor.fetchone()

        self.division_id = row["divisionID"]
        self.corporation_id = row["corporationID"]
        self.location_id = row["locationID"]
        self.level = row["level"]
        self.quality = row["quality"]
        self.agent_type_id = row["agentTypeID"]

        cursor.close()
