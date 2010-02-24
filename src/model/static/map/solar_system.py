'''
Created on Oct 28, 2009

@author: frederikns
'''
from model.static.map import map_dictionaries
from model.static.inv import inventory_dictionaries
from model.static.database import database

class SolarSystem(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EIKGdhEREd-LgJ4IxcJkTA
    """

    def __init__(self, solar_system_id):
        self.solar_system_id = solar_system_id
        
        cursor = database.get_cursor("select * from mapSolarSystem where \
        solarSystemID=%s;" % (self.solar_system_id))
        row = cursor.fetchone()
        
        self.region_id = row["regionID"]
        self.constellation_id = row["constellationID"]
        self.solar_system_name = row["solarSystemName"]
        self.x_pos = row["x"]
        self.y_pos = row["y"]
        self.z_pos = row["z"]
        self.x_min = row["xMin"]
        self.x_max = row["xMax"]
        self.y_min = row["yMin"]
        self.y_ax = row["yMax"]
        self.z_min = row["zMin"]
        self.z_max = row["zMax"]
        self.luminosity = row["luminosity"]
        self.border = row["border"]
        self.fringe = row["fringe"]
        self.corridor = row["corridor"]
        self.hub = row["hub"]
        self.international = row["international"]
        self.regional = row["regional"]
        self.constellation = row["constellation"]
        self.security = row["security"]
        self.faction_id = row["factionID"]
        self.radius = row["radius"]
        self.sun_type_id = row["sunTypeID"]
        self.security_class = row["securityClass"]
        
        cursor.close()
        
        self.region = None
        self.constellation = None
        self.sun_type = None
        
    def get_region(self):
        """Populates and returns the region"""
        if self.region is None:
            self.region = map_dictionaries.get_region(self.region_id)
        return self.region
    
    def get_constellation(self):
        """Populates and returns the constellation"""
        if self.constellation is None:
            self.constellation = map_dictionaries.\
            get_constellation(self.constellation_id)
        return self.constellation
    
    def get_sun_type(self):
        """Populates and returns the sun type"""
        if self.sun_type is None:
            self.sun_type = inventory_dictionaries.get_type(self.sun_type_id)
        return self.sun_type
