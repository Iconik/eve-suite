'''
Created on Oct 28, 2009

@author: frederikns
'''
from model.flyweight import Flyweight
from model.static.database import database

class SolarSystem(Flyweight):
    def __init__(self, solar_system_id):
        #prevents reinitializing
        if "inited" in self.__dict__:
            return
        self.inited = None
        #prevents reinitializing
        
        self.solar_system_id = solar_system_id
        
        cursor = database.get_cursor("select * from mapSolarSystems where \
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
            from model.static.map.region import Region
            self.region = Region(self.region_id)
        return self.region
    
    def get_constellation(self):
        """Populates and returns the constellation"""
        if self.constellation is None:
            from model.static.map.constellation import Constellation
            self.constellation = Constellation(self.constellation_id)
        return self.constellation
    
    def get_sun_type(self):
        """Populates and returns the sun type"""
        if self.sun_type is None:
            from model.static.inv.type import Type
            self.sun_type = Type(self.sun_type_id)
        return self.sun_type
    
    def __str__(self):
        return self.solar_system_name