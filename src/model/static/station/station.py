'''
Created on Oct 28, 2009

@author: frederikns
'''

from model.static.database import database
from model.static.map import map_dictionaries
from model.static.inventory import inventory_dictionaries

class Station(object):
    '''
    classdocs
    '''


    def __init__(self,id):
        '''
        Constructor
        '''
        self.station_id = id
        
        cursor = database.get_cursor("select * from mapSolarSystem where solarSystemID='%s';" % (self.solarSystemID))
        row = cursor.fetchone()
        
        self.security = row["security"]
        self.docking_cost_per_volume = row["dockingCostPervolume"]
        self.max_ship_volume_dockable = row["maxShipVolumeDockable"]
        self.office_rental_cost = row["officeRentalCost"]
        self.operation_id = row["operationID"]
        self.station_type_id = row["stationTypeID"]
        self.corporation_id = row["corporationID"]
        self.solar_system_id = row["solarSystemID"]
        self.constellation_id = row["constellationID"]
        self.region_id = row["regionID"]
        self.station_name = row["stationName"]
        self.x = row["x"]
        self.y = row["y"]
        self.z = row["z"]
        self.reprocessing_efficiency = row["reprocessingEfficiency"]
        self.reprocessing_stations_take = row["reprocessingStationsTake"]
        self.reprocessing_hangar_flag = row["reprocessingHangarFlag"]
        
        cursor.close()
        
    def get_solar_system(self):
        if 'self.solar_system' not in locals():
            self.solar_system = map_dictionaries.get_solar_system(self.solar_system_id)
        return self.solar_system
        
    def get_region(self):
        if 'self.region' not in locals():
            self.region = map_dictionaries.get_region(self.region_id)
        return self.region
    
    def get_constellation(self):
        if 'self.constellation' not in locals():
            self.constellation = map_dictionaries.get_constellation(self.constellation_id)
        return self.constellation
    
    def get_sun_type(self):
        if 'self.station_type' not in locals():
            self.station_type = inventory_dictionaries.get_type(self.station_type_id)
        return self.station_type