'''
Created on Nov 26, 2009

@author: frederikns
'''
import sqlite3

class MarketGroup(object):
    '''
    classdocs
    '''


    def __init__(self,marketGroupID):
        '''
        Constructor
        '''
        
        self.marketGroupID = marketGroupID
        conn = sqlite3.connect('../../../Resources/Database/apo15-sqlite3-v1.db')
        cur = conn.cursor()
        cur.execute("select * from invTypes where marketGroupID='%s';" % (self.marketGroupID))
        row = cur.fetchone()
        
        self.parentGroupID = row[1]
        self.marketGroupName = row[2]
        self.description = row[3]
        self.graphicsID = row[4]
        self.hasTypes = row[5]
        
        cur.close()
        conn.close()