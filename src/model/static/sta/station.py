'''
Created on Oct 28, 2009

@author: frederikns
'''

from model.static.database import database
from model.static.map import map_dictionaries
from model.static.inv import inventory_dictionaries

class Station(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EIPmCBEREd-LgJ4IxcJkTA
    """

    def __init__(self, station_id):
        self.station_id = station_id
        
        cursor = database.get_cursor("select * from staStations where \
        stationID='%s';" % (self.station_id))
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
        self.x_pos = row["x"]
        self.y_pos = row["y"]
        self.z_pos = row["z"]
        self.reprocessing_efficiency = row["reprocessingEfficiency"]
        self.reprocessing_stations_take = row["reprocessingStationsTake"]
        self.reprocessing_hangar_flag = row["reprocessingHangarFlag"]
        
        cursor.close()
        
        self.solar_system = None
        self.region = None
        self.constellation = None
        self.station_type = None
        
    def get_solar_system(self):
        """Populations and returns the solar system"""
        if self.solar_system is None:
            self.solar_system = map_dictionaries.\
            get_solar_system(self.solar_system_id)
        return self.solar_system
        
    def get_region(self):
        """Populations and returns the region"""
        if self.region is None:
            self.region = map_dictionaries.get_region(self.region_id)
        return self.region
    
    def get_constellation(self):
        """Populations and returns the constellation"""
        if self.constellation is None:
            self.constellation = map_dictionaries.\
            get_constellation(self.constellation_id)
        return self.constellation
    
    def get_stations_type(self):
        """Populations and returns the station type"""
        if self.station_type is None:
            self.station_type = inventory_dictionaries.\
            get_type(self.station_type_id)
        return self.station_type
