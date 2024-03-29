from model.flyweight import Flyweight
from model.static.database import database

class LocationScene(Flyweight):
    def __init__(self,location_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.location_id = location_id

        cursor = database.get_cursor(
            "select * from mapLocationScenes where locationID={};".format(
                self.location_id))
        row = cursor.fetchone()

        self.scene_id = row["sceneID"]

        cursor.close()
