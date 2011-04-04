from model.flyweight import Flyweight
from model.static.database import database

class Attribute(Flyweight):
    def __init__(self,attribute_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.attribute_id = attribute_id

        cursor = database.get_cursor("select * from chrAttributes where \
        attributeID=%s;" % (self.attribute_id))
        row = cursor.fetchone()

        self.attribute_name = row["attributeName"]
        self.description = row["description"]
        self.icon_id = row["iconID"]
        self.short_description = row["shortDescription"]
        self.notes = row["notes"]

        cursor.close()
