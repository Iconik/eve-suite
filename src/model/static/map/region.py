from model.flyweight import Flyweight
from model.static.database import database

class Region(Flyweight):
    def __init__(self, region_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.region_id = region_id

        cursor = database.get_cursor("select * from mapLocationScenes where \
        locationID=%s;" % (self.location_id))
        row = cursor.fetchone()

        self.region_name = row["regionName"]
        self.x = row["x"]
        self.y = row["y"]
        self.z = row["z"]
        self.x_min = row["xMin"]
        self.x_max = row["xMax"]
        self.y_min = row["yMin"]
        self.y_max = row["yMax"]
        self.z_min = row["zMin"]
        self.z_max = row["zMax"]
        self.faction_id = row["factionID"]
        self.radius = row["radius"]

        cursor.close()
