from model.flyweight import Flyweight
from model.static.database import database

class Relationship(Flyweight):
    def __init__(self, relationship_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.relationship_id = relationship_id
        
        cursor = database.get_cursor("select * from crtRelationships where \
        relationshipID=%s;" % (self.relationship_id))
        row = cursor.fetchone()
        
        self.parent_id = row["parentID"]
        self.parent_type_id = row["parentTypeID"]
        self.parent_level = row["parentLevel"]
        self.child_id = row["childID"]
        
        self._parent = None
        self._parent_type = None
        self._child = None
        
    def get_parent(self):
        if self._parent is None:
            from model.static.crt.certificate import Certificate
            self._parent = Certificate(self.parent_id)
        return self._parent
    
    def get_parent_type(self):
        if self._parent_type is None:
            from model.static.inv.type import Type
            self._parent_type = Type(self.parent_type_id)
        return self._parent_type
    
    def get_child(self):
        if self._child is None:
            from model.static.crt.certificate import Certificate
            self._child = Certificate(self.child_id)
        return self._child