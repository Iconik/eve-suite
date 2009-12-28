'''
Created on Nov 26, 2009

@author: frederikns
'''
from model.static.inventory.category import Category
from model.static.database import database
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
        
        cursor = database.get_cursor("select * from invGroups where groupID=%s;" % (self.groupID))
        row = cursor.fetchone()
        
        self.categoryID = row["categoryID"]
        self.groupName = row["groupName"]
        self.description = row["description"]
        self.graphicID = row["graphicID"]
        self.useBasePrice = row["useBasePrice"]
        self.allowManufacture = row["allowManufacture"]
        self.allowRecycler = row["allowRecycler"]
        self.anchored = row["anchored"]
        self.anchorable = row["anchorable"]
        self.fittableNonSingleton = row["fittableNonSingleton"]
        self.published = row["published"]
        
        cursor.close()
        