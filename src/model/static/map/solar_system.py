'''
Created on Oct 28, 2009

@author: frederikns
'''
from model.static.map import map_dictionaries
from model.static.inventory import inventory_dictionaries
from model.static.database import database

class SolarSystem(object):
    '''
    classdocs
    '''

    def __init__(self,solar_system_id):
        '''
        Constructor
        '''
        self.solar_system_id = solar_system_id
        
        cursor = database.get_cursor("select * from mapSolarSystem where solarSystemID='%s';" % (self.solar_system_id))
        row = cursor.fetchone()
        
        self.region_id = row["regionID"]
        self.constellation_id = row["constellationID"]
        self.solar_system_name = row["solarSystemName"]
        self.x = row["x"]
        self.y = row["y"]
        self.z = row["z"]
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
        
    def get_region(self):
        if 'self.region' not in locals():
            self.region = map_dictionaries.get_region(self.region_id)
        return self.region
    
    def get_constellation(self):
        if 'self.constellation' not in locals():
            self.constellation = map_dictionaries.get_constellation(self.constellation_id)
        return self.constellation
    
    def get_sun_type(self):
        if 'self.sun_type' not in locals():
            self.sun_type = inventory_dictionaries.get_type(self.sun_type_id)
        return self.sun_type