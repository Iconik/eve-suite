'''
Created on Feb 7, 2010

@author: frederikns
'''
from model.static.database import database
from model.flyweight import Flyweight
from model.static.crt.certificate_category import CertificateCategory
from model.static.crt.certificate_class import CertificateClass
from model.static.crp.npc_corporation import NPCCorporation

class Certificate(Flyweight):
    def __init__(self, certificate_id):
        #prevents reinitializing
        if "inited" in self.__dict__:
            return
        self.inited = None
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
        
        self.category = None
        self.certificate_class = None
        self.corporation = None
        
    def get_category(self):
        if self.category is None:
            self.category = CertificateCategory(self.certificate_id)
        return self.category
    
    def get_certificate_class(self):
        if self.certificate_class is None:
            self.certificate_class = CertificateClass(self.certificate_class_id)
        return self.certificate_class
    
    def get_corporation(self):
        if self.corporation is None:
            self.corporation = NPCCorporation(self.corporation_id)
        return self.corporation