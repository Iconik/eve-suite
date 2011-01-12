'''
Created on Nov 26, 2009

@author: frederikns
'''
from model.static.database import database
from model.flyweight import Flyweight
from model.static.inv.category import Category

class Group(Flyweight):
    def __init__(self, group_id):
        #prevents reinitializing
        if "inited" in self.__dict__:
            return
        self.inited = None
        #prevents reinitializing

        self.group_id = group_id
        
        cursor = database.get_cursor("select * from invGroups where \
        groupID=%s;" % (self.group_id))
        row = cursor.fetchone()
        
        self.category_id = row["categoryID"]
        self.group_name = row["groupName"]
        self.description = row["description"]
        self.graphic_id = row["graphicID"]
        self.use_base_price = row["useBasePrice"]
        self.allow_manufacture = row["allowManufacture"]
        self.allow_recycler = row["allowRecycler"]
        self.anchored = row["anchored"]
        self.anchorable = row["anchorable"]
        self.fittable_non_singleton = row["fittableNonSingleton"]
        self.published = row["published"]
        
        cursor.close()
        
        self.category = None
    
    def get_category(self):
        """Populates and returns the category"""
        if self.category is None:
            self.category = Category(self.category_id)
        return self.category
