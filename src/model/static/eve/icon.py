from model.flyweight import Flyweight
from model.static.database import database

class Icon(Flyweight):
    def __init__(self,icon_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.icon_id = icon_id

        cursor = database.get_cursor(
            "select * from eveIcons where iconID={};".format(self.icon_id))
        row = cursor.fetchone()

        self.icon_file = row["iconFile"]
        self.description = row["description"]

        cursor.close()
