'''
Created on Nov 26, 2009

@author: frederikns
'''
from Model.Inventory.Category import Category
import sqlite3

class Group(object):
    '''
    classdocs
    '''


    def __init__(self,groupID):
        '''
        Constructor
        '''
        self.groupID = groupID
        conn = sqlite3.connect('../../../Resources/Database/apo15-sqlite3-v1.db')
        cur = conn.cursor()
        cur.execute("select * from invTypes where groupID='%s';" % (self.groupID))
        row = cur.fetchone()
        
        self.categoryID = row[1]
        self.groupName = row[2]
        self.description = row[3]
        self.graphicID = row[4]
        self.useBasePrice = row[5]
        self.allowManufacture = row[6]
        self.allowRecycler = row[7]
        self.anchored = row[8]
        self.anchorable = row[9]
        self.fittableNonSingleton = row[9]
        self.published = row[10]
        
        cur.close()
        conn.close()
        
    def get_categoryID(self):
        return self.categoryID
    
    def get_category(self):
        if self.category is None:
            self.category = Category(self.categoryID)
        return self.category
        