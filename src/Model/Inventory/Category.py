'''
Created on Nov 26, 2009

@author: frederikns
'''
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
        
        conn = sqlite3.connect('../../../Resources/Database/apo15-sqlite3-v1.db')
        cur = conn.cursor()
        cur.execute("select * from invTypes where categoryID='%s';" % (self.categoryID))
        row = cur.fetchone()
        
        self.categoryName = row[1]
        self.description = row[2]
        self.graphicID = row[3]
        self.published = row[4]