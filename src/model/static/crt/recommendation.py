from model.flyweight import Flyweight
from model.static.database import database

class Recommendation(Flyweight):
    def __init__(self,recommendation_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.recommendation_id = recommendation_id
        
        cursor = database.get_cursor("select * from crtRecommendations where \
        recommendationID=%s;" % (self.recommendation_id))
        row = cursor.fetchone()
        
        self.ship_type_id = row["shipTypeID"]
        self.certificate_id = row["certificateID"]
        self.recommendation_level = row["recommendationLevel"]
        
        self._ship_type = None
        self._certificate = None
        
    def get_ship_type(self):
        if self._ship_type is None:
            from model.static.inv.type import Type
            self._ship_type = Type(self.ship_type_id)
        return self._ship_type
    
    def get_certificate(self):
        if self._certificate is None:
            from model.static.crt.certificate import Certificate
            self._certificate = Certificate(self.certificate_id)
        return self._certificate