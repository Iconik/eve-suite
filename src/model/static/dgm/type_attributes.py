'''
Created on 30 Jan 2010

@author: FrederikNS
'''
from model.flyweight import Flyweight
from model.static.database import database
from model.static.dgm.attribute import Attribute

class TypeAttributes(Flyweight):
    def __init__(self, type_id):
        #prevents reinitializing
        if "inited" in self.__dict__:
            return
        self.inited = None
        #prevents reinitializing
        
        self.type_id = type_id
        
        cursor = database.get_cursor("select * from dgmTypeAttributes where \
        typeID=%s;" % (self.type_id))
        
        self.attributes = list()
        
        for row in cursor:
            if row["valueInt"] is not None:
                self.attributes.append((Attribute(row["attributeID"]),
                                     row["valueInt"]))
            elif row["valueFloat"] is not None:
                self.attributes.append((Attribute(row["attributeID"]),
                                     row["valueFloat"]))
        
        cursor.close()
