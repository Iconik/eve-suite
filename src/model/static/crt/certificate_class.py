from model.static.database import database
from model.flyweight import Flyweight

class CertificateClass(Flyweight):
    def __init__(self, class_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing
        
        self.class_id = class_id
        
        cursor = database.get_cursor("select * from crtClasses where \
        classID=%s;" % (self.class_id))
        row = cursor.fetchone()
        
        self.description = row["description"]
        self.class_name = row["className"]