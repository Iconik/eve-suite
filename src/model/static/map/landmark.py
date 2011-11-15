from model.flyweight import Flyweight
from model.static.database import database

class Landmark(Flyweight):
    def __init__(self,landmark_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.landmark_id = landmark_id

        cursor = database.get_cursor(
            "select * from mapLandmark where landmarkID={};".format(
                self.landmark_id))
        row = cursor.fetchone()

        self.landmark_name = row["landmarkName"]
        self.description = row["description"]
        self.location_id = row["locationID"]
        self.x = row["x"]
        self.y = row["y"]
        self.z = row["z"]
        self.radius = row["radius"]
        self.icon_id = row["iconID"]
        self.importance = row["importance"]

        cursor.close()
