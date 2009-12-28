'''
Created on Oct 28, 2009

@author: frederikns
'''
from model.static.database import database
from model.static.map import map_dictionaries
from model.static.character import character_dictionaries

class Constellation(object):
    '''
    classdocs
    '''

    def __init__(self,constellation_id):
        '''
        Constructor
        '''
        self.constellation_id = constellation_id
        
        cursor = database.get_cursor("select * from mapConstellations where constellationID='%s';" % (self.constellation_id))
        row = cursor.fetchone()
        
        self.region_id = row["regionID"]
        self.constellation_name = row["constellationName"]
        self.x = row["x"]
        self.y = row["y"]
        self.z = row["z"]
        self.x_min = row["xMin"]
        self.x_max = row["xMax"]
        self.y_min = row["yMin"]
        self.y_max = row["yMax"]
        self.z_min = row["zMin"]
        self.z_max = row["zMax"]
        self.faction_id = row["factionID"]
        self.radius = row["radius"]
        
    def get_region(self):
        if 'self.region' not in locals():
            self.region = map_dictionaries.get_region(self.region_id)
        return self.region
    
    def get_faction(self):
        if 'self.faction' not in locals():
            self.faction = character_dictionaries.get_faction(self.faction_id)
        return self.faction