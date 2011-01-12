'''
Created on 23 Dec 2009

@author: FrederikNS
'''
from model.static.database import database
from model.flyweight import Flyweight

class Race(Flyweight):
    def __init__(self, race_id):
        #prevents reinitializing
        if "inited" in self.__dict__:
            return
        self.inited = None
        #prevents reinitializing
        
        self.race_id = race_id
        
        cursor = database.get_cursor("select * from chrRaces where \
        raceID='%s';" % (self.race_id))
        row = cursor.fetchone()
        
        self.race_name = row["raceName"]
        self.description = row["description"]
        self.graphic_id = row["graphicID"]
        self.short_description = row["shortDescription"]
