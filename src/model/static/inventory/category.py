'''
Created on Nov 26, 2009

@author: frederikns
'''
from model.static.database import database

import sqlite3

class Category(object):
    '''
    classdocs
    '''

    def __init__(self,categoryID):
        '''
        Constructor
        '''
        self.categoryID = categoryID
        
        cursor = database.get_cursor("select * from invTypes where categoryID=%s;" % (self.categoryID))
        row = cursor.fetchone()
        
        self.categoryName = row["categoryName"]
        self.description = row["description"]
        self.graphicID = row["graphicID"]
        self.published = row["published"]
        
        cursor.close()