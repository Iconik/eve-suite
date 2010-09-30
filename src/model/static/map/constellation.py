'''
Created on Oct 28, 2009

@author: frederikns
'''
from model.static.database import database
from model.static.map import map_dictionaries
from model.static.chr import character_dictionaries

class Constellation(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EIHqOBEREd-LgJ4IxcJkTA
    """

    def __init__(self, constellation_id):
        '''
        Constructor
        '''
        self.constellation_id = constellation_id
        
        cursor = database.get_cursor("select * from mapConstellations where \
        constellationID='%s';" % (self.constellation_id))
        row = cursor.fetchone()
        
        self.region_id = row["regionID"]
        self.constellation_name = row["constellationName"]
        self.x_pos = row["x"]
        self.y_pos = row["y"]
        self.z_pos = row["z"]
        self.x_min = row["xMin"]
        self.x_max = row["xMax"]
        self.y_min = row["yMin"]
        self.y_max = row["yMax"]
        self.z_min = row["zMin"]
        self.z_max = row["zMax"]
        self.faction_id = row["factionID"]
        self.radius = row["radius"]
        
        self.region = None
        self.faction = None
        
    def get_region(self):
        """Populates and returns the region"""
        if self.region is None:
            self.region = map_dictionaries.get_region(self.region_id)
        return self.region
    
    def get_faction(self):
        """Populates and returns the faction"""
        if self.faction is None:
            self.faction = character_dictionaries.get_faction(self.faction_id)
        return self.faction
