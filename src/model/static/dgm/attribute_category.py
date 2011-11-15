from model.flyweight import Flyweight
from model.static.database import database

class AttributeCategory(Flyweight):
    def __init__(self,category_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.category_id = category_id

        cursor = database.get_cursor(
            "select * from dgmAttributeCategories where categoryID={};".format(
                self.category_id))
        row = cursor.fetchone()

        self.category_name = row["categoryName"]
        self.category_description = row["categoryDescription"]

        cursor.close()
