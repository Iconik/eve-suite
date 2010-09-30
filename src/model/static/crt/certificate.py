'''
Created on Feb 7, 2010

@author: frederikns
'''
from model.static.database import database
from model.static.crt import certificate_dictionaries
from model.static.crp import corporation_dictionaries

class Certificate(object):
    '''
    classdocs
    '''

    def __init__(self, certificate_id):
        '''
        Constructor
        '''
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
            self.category = \
            certificate_dictionaries.get_category(self.certificate_id)
        return self.category
    
    def get_certificate_class(self):
        if self.certificate_class is None:
            self.certificate_class = \
            certificate_dictionaries.get_certificate_class(self.certificate_class_id)
        return self.certificate_class
    
    def get_corporation(self):
        if self.corporation is None:
            self.corporation = \
            corporation_dictionaries.get_npc_corporation(self.corporation_id)
        return self.corporation