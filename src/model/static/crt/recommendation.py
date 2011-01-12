'''
Created on Feb 7, 2010

@author: frederikns
'''
from model.static.database import database
from model.static.inv.type import Type
from model.static.crt.certificate import Certificate
from model.flyweight import Flyweight

class Recommendation(Flyweight):
    def __init__(self,recommendation_id):
        #prevents reinitializing
        if "inited" in self.__dict__:
            return
        self.inited = None
        #prevents reinitializing

        self.recommendation_id = recommendation_id
        
        cursor = database.get_cursor("select * from crtRecommendations where \
        recommendationID=%s;" % (self.recommendation_id))
        row = cursor.fetchone()
        
        self.ship_type_id = row["shipTypeID"]
        self.certificate_id = row["certificateID"]
        self.recommendation_level = row["recommendationLevel"]
        
        self.ship_type = None
        self.certificate = None
        
    def get_ship_type(self):
        if self.ship_type is None:
            self.ship_type = Type(self.ship_type_id)
        return self.ship_type
    
    def get_certificate(self):
        if self.certificate is None:
            self.certificate = Certificate(self.certificate_id)
        return self.certificate