from model.flyweight import Flyweight
from model.static.database import database

class Graphic(Flyweight):
    def __init__(self,graphic_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.graphic_id = graphic_id

        cursor = database.get_cursor("select * from eveGraphics where \
        graphicID=%s;" % (self.graphic_id))
        row = cursor.fetchone()

        self.graphic_file = row["graphicFile"]
        self.description = row["description"]
        self.obsolete = True if row["obsolete"] == 1 else False
        self.graphic_type = row["graphicType"]
        self.collidable = True if row["collidable"] == 1 else False
        self.explosion_id = row["explosionID"]
        self.directory_id = row["directoryID"]
        self.graphic_name = row["graphicName"]

        cursor.close()
