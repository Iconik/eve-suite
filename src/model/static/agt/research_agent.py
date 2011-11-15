from model.flyweight import Flyweight
from model.static.database import database

class ResearchAgent(Flyweight):
    def __init__(self,agent_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.agent_id = agent_id

        cursor = database.get_cursor(
            "select * from agtResearchAgents where agentID={};".format(
                self.agent_id))
        
        self.types = list()
        
        for row in cursor:
            self.types.append(row["typeID"])

        cursor.close()
