'''
Created on Nov 26, 2009

@author: frederikns
'''
from model.static.database import database
from model.flyweight import Flyweight

class Category(Flyweight):
    def __init__(self, category_id):
        #prevents reinitializing
        if "inited" in self.__dict__:
            return
        self.inited = None
        #prevents reinitializing
        
        self.category_id = category_id
        
        cursor = database.get_cursor("select * from invCategories where \
        categoryID=%s;" % (self.category_id))
        row = cursor.fetchone()
        
        self.category_name = row["categoryName"]
        self.description = row["description"]
        self.graphic_id = row["graphicID"]
        self.published = row["published"]
        
        cursor.close()
