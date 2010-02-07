'''
Created on Nov 26, 2009

@author: frederikns
'''
from model.static.database import database

class Category(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EIA8hhEREd-LgJ4IxcJkTA
    """

    def __init__(self, category_id):
        '''
        Constructor
        '''
        self.category_id = category_id
        
        cursor = database.get_cursor("select * from invTypes where \
        categoryID=%s;" % (self.category_id))
        row = cursor.fetchone()
        
        self.category_name = row["categoryName"]
        self.description = row["description"]
        self.graphic_id = row["graphicID"]
        self.published = row["published"]
        
        cursor.close()
