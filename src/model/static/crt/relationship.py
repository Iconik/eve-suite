'''
Created on Feb 7, 2010

@author: frederikns
'''
from model.static.database import database
from model.static.crt import certificate_dictionaries
from model.static.inv import inventory_dictionaries

class Relationship(object):
    '''
    classdocs
    '''


    def __init__(self, relationship_id):
        '''
        Constructor
        '''
        self.relationship_id = relationship_id
        
        cursor = database.get_cursor("select * from crtRelationships where \
        relationshipID=%s;" % (self.relationship_id))
        row = cursor.fetchone()
        
        self.parent_id = row["parentID"]
        self.parent_type_id = row["parentTypeID"]
        self.parent_level = row["parentLevel"]
        self.child_id = row["childID"]
        
        self.parent = None
        self.parent_type = None
        self.child = None
        
    def get_parent(self):
        if self.parent is None:
            self.parent = \
            certificate_dictionaries.get_certificate(self.parent_id)
        return self.parent
    
    def get_parent_type(self):
        if self.parent_type is None:
            self.parent_type = \
            inventory_dictionaries.get_type(self.parent_type_id)
        return self.parent_type
    
    def get_child(self):
        if self.child is None:
            self.child = \
            certificate_dictionaries.get_certificate(self.child_id)
        return self.child