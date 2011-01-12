'''
Created on 30 Jan 2010

@author: FrederikNS
'''
from model.flyweight import Flyweight
from model.static.database import database

class Attribute(Flyweight):
    def __init__(self, attribute_id):
        #prevents reinitializing
        if "inited" in self.__dict__:
            return
        self.inited = None
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
        
        self.category = None

    def get_category(self):
        """Populates and returns the category"""
        if self.category is None:
            from model.static.inv.category import Category
            self.category = Category(self.category_id)
        return self.category