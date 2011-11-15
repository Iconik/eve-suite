from model.flyweight import Flyweight
from model.static.database import database

class Jump(Flyweight):
    def __init__(self,stargate_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.stargate_id = stargate_id

        cursor = database.get_cursor(
            "select * from mapJumps where stargateID={};".format(
                self.stargate_id))
        row = cursor.fetchone()

        self.celestial_id = row["celestialID"]

        cursor.close()
