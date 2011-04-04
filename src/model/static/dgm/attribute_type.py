from model.flyweight import Flyweight
from model.static.database import database

class AttributeType(Flyweight):
    def __init__(self, attribute_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.attribute_id = attribute_id

        cursor = database.get_cursor("select * from dgmAttributeTypes where \
        attributeID=%s;" % (self.attribute_id))
        row = cursor.fetchone()

        self.attribute_name = row["attributeName"]
        self.description = row["description"]
        self.graphic_id = row["graphicID"]
        self.default_value = row["defaultValue"]
        self.published = row["published"]
        self.display_name = row["displayName"]
        self.unit_id = row["unitID"]
        self.stackable = row["stackable"]
        self.high_is_good = row["highIsGood"]
        self.category_id = row["categoryID"]

        cursor.close()

        self._category = None

    def get_category(self):
        """Populates and returns the _category"""
        if self._category is None:
            from model.static.inv.category import Category
            self._category = Category(self.category_id)
        return self._category
