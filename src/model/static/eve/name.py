from model.flyweight import Flyweight
from model.static.database import database

class Name(Flyweight):
    def __init__(self,item_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.item_id = item_id

        cursor = database.get_cursor("select * from eveNames where \
        itemID=%s;" % (self.item_id))
        row = cursor.fetchone()

        self.item_name = row["itemName"]
        self.category_id = row["categoryID"]
        self.group_id = row["groupID"]
        self.type_id = row["typeID"]

        cursor.close()
