from model.flyweight import Flyweight
from model.static.database import database

class Ancestry(Flyweight):
    def __init__(self,ancestry_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.ancestry_id = ancestry_id

        cursor = database.get_cursor(
            "select * from chrAncestries where ancestryID={};".format(
                self.ancestry_id))
        row = cursor.fetchone()

        self.ancestry_name = row["ancestryName"]
        self.bloodline_id = row["bloodlineID"]
        self.description = row["description"]
        self.perception = row["perception"]
        self.willpower = row["willpower"]
        self.charisma = row["charisma"]
        self.memory = row["memory"]
        self.intelligence = row["intelligence"]
        self.icon_id = row["iconID"]
        self.short_description = row["shortDescription"]

        cursor.close()
