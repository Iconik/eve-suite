'''
Created on Feb 7, 2010

@author: frederikns
'''
from model.static.database import database
from model.flyweight import Flyweight

class CertificateCategory(Flyweight):
    def __init__(self, category_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing
        
        self.category_id = category_id
        
        cursor = database.get_cursor("select * from crtCategories where \
        categoryID=%s;" % (self.category_id))
        row = cursor.fetchone()
        
        self.description = row["description"]
        self.category_name = row["categoryName"]