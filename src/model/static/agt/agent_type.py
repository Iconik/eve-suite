from model.flyweight import Flyweight
from model.static.database import database

class AgentType(Flyweight):
    def __init__(self,agent_type_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.agent_type_id = agent_type_id

        cursor = database.get_cursor(
            "select * from agtAgentTypes where agentTypeID={};".format(
                self.agent_type_id))
        row = cursor.fetchone()

        self.agent_type = row["agentType"]

        cursor.close()
