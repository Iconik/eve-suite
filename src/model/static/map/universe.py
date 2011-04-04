from model.flyweight import Flyweight
from model.static.database import database

class Universe(Flyweight):
    def __init__(self,universe_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.universe_id = universe_id

        cursor = database.get_cursor("select * from mapUniverse where \
        universeID=%s;" % (self.universe_id))
        row = cursor.fetchone()

        self.universe_name = row["universeName"]
        self.x = row["x"]
        self.y = row["y"]
        self.z = row["z"]
        self.x_min = row["xMin"]
        self.x_max = row["xMax"]
        self.y_min = row["yMin"]
        self.y_max = row["yMax"]
        self.z_min = row["zMin"]
        self.z_max = row["zMax"]
        self.radius = row["radius"]

        cursor.close()
