from model.flyweight import Flyweight
from model.static.database import database

class ControlTowerResourcePurpose(Flyweight):
    def __init__(self,purpose):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.purpose = purpose

        cursor = database.get_cursor(
            "select * from invControlTowerResourcePurposes where purpose={};".format(self.purpose))
        row = cursor.fetchone()

        self.purpose_text = row["purposeText"]

        cursor.close()
