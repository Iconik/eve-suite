'''
Created on Feb 7, 2010

@author: frederikns
'''
from model.static.database import database

class CertificateClass(object):
    '''
    classdocs
    '''

    def __init__(self, class_id):
        '''
        Constructor
        '''
        
        self.class_id = class_id
        
        cursor = database.get_cursor("select * from crtClasses where \
        classID=%s;" % (self.class_id))
        row = cursor.fetchone()
        
        self.description = row["description"]
        self.class_name = row["className"]