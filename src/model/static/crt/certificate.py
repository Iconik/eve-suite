from model.flyweight import Flyweight
from model.static.database import database

class Certificate(Flyweight):
    def __init__(self, certificate_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing
        
        self.certificate_id = certificate_id
        
        cursor = database.get_cursor("select * from crtCertificates where \
        certificateID=%s;" % (self.certificate_id))
        row = cursor.fetchone()
        
        self.category_id = row["categoryID"]
        self.certificate_class_id = row["classID"]
        self.grade = row["grade"]
        self.corporation_id = row["corpID"]
        self.icon_id = row["iconID"]
        self.description = row["description"]
        
        self._category = None
        self._certificate_class = None
        self._corporation = None
        
    def get_category(self):
        if self._category is None:
            from model.static.crt.certificate_category import CertificateCategory
            self._category = CertificateCategory(self.certificate_id)
        return self._category
    
    def get_certificate_class(self):
        if self._certificate_class is None:
            from model.static.crt.certificate_class import CertificateClass
            self._certificate_class = CertificateClass(self.certificate_class_id)
        return self._certificate_class
    
    def get_corporation(self):
        if self._corporation is None:
            from model.static.crp.npc_corporation import NPCCorporation
            self._corporation = NPCCorporation(self.corporation_id)
        return self._corporation