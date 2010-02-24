'''
Created on Feb 7, 2010

@author: frederikns
'''
from model.static.database import database

class Category(object):
    '''
    classdocs
    '''


    def __init__(self, category_id):
        '''
        Constructor
        '''
        self.category_id = category_id
        
        cursor = database.get_cursor("select * from crtCategories where \
        categoryID=%s;" % (self.category_id))
        row = cursor.fetchone()
        
        self.description = row["description"]
        self.category_name = row["categoryName"]