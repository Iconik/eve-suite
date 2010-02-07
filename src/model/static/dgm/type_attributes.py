'''
Created on 30 Jan 2010

@author: FrederikNS
'''

from model.static.database import database
from model.static.dgm import dgm_dictionaries

class TypeAttributes(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EH-gRREREd-LgJ4IxcJkTA
    """

    def __init__(self, type_id):
        '''
        Constructor
        '''
        self.type_id = type_id
        
        cursor = database.get_cursor("select * from dgmTypeAttributes where \
        typeID=%s;" % (self.type_id))
        
        self.attributes = list()
        
        for row in cursor:
            if row["valueInt"] is not None:
                self.attributes.append((dgm_dictionaries.\
                                     get_attribute(row["attributeID"]),
                                     row["valueInt"]))
            elif row["valueFloat"] is not None:
                self.attributes.append((dgm_dictionaries.\
                                     get_attribute(row["attributeID"]),
                                     row["valueFloat"]))
        
        cursor.close()
