'''
Created on Oct 28, 2009

@author: frederikns
'''
import sqlite3

class Type(object):
    '''
    classdocs
    '''

    def __init__(self,id):
        '''
        Constructor
        '''
        self.typeID = id
        conn = sqlite3.connect('../../../Resources/Database/apo15-sqlite3-v1.db')
        cur = conn.cursor()
        cur.execute("select * from invTypes where typeID='%s';" % (self.typeID))
        row = cur.fetchone()
        
        self.groupID = row[1]
        self.typeName = row[2]
        self.description = row[3]
        self.graphicID = row[4]
        self.radius = row[5]
        self.mass = row[6]
        self.volume = row[7]
        self.capacity = row[8]
        self.portionSize = row[9]
        self.raceID = row[10]
        self.basePrice = row[11]
        self.published = row[12]
        self.marketGroupID = row[13]
        self.chanceOfDuplicating = row[14]
        
        cur.close()
        conn.close()
        
    def get_typeID(self):
        return self.typeID
    
    def get_groupID(self):
        return self.groupID
    
    def get_typeName(self):
        return self.typeName
    
    def get_description(self):
        return self.description
    
    def get_graphicID(self):
        return self.graphicID
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return self.volume
    
    def get_capacity(self):
        return self.capacity
    
    def get_portionSize(self):
        return self.portionSize
    
    def get_raceID(self):
        return self.raceID
    
    def get_basePrice(self):
        return self.basePrice
    
    def get_published(self):
        return self.published
    
    def get_marketGroupID(self):
        return self.marketGroupID
    
    def get_chanceOfDuplicating(self):
        return self.chanceOfDuplicating

if __name__ == '__main__':
    ite = Type(587)
    print(ite.toString())

"""
import sys
from xml.etree.ElementTree import ElementTree
import sqlite3

conn = sqlite3.connect('../../../../EVE Suite/Resources/Database/apo15-sqlite3-v1.db')
c = conn.cursor()
root = ElementTree(file="../../AssetList.xml.aspx")
iter = root.getiterator()
for element in iter:
    #print("Element:", element.tag)
    if element.keys():
        #print("\tAttributes:")
        for name, value in element.items():
            #print("\t\tName: '%s', Value: '%s'"%(name, value))
            if name == 'typeID':
                c.execute("select typeName from invTypes where typeID='"+value+"'")
                print("\n\t\t\t"+str(c.fetchone()))
            if name == "locationID":
                c.execute("select stationName from staStations where stationID='"+value+"'")
                print("\t\t\t"+str(c.fetchone()))
    #print("\tChildren:")
    if element.text:
        text = element.text
        text = len(text) > 40 and text[:40] + "..." or text
        #print("\t\tText:", repr(text))
    if element.getchildren():
        for child in element:
            #print("\t\tElement", child.tag)
            if child.tail:
                text = child.tail
                text = len(text) > 40 and text[:40] + "..." or text
                #print("\t\tText:", repr(text))
"""