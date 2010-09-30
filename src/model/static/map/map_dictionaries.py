'''
Created on Nov 26, 2009

@author: frederikns
'''
from weakref import WeakValueDictionary

CONSTELLATIONS = WeakValueDictionary()
REGIONS = WeakValueDictionary()
SOLAR_SYSTEMS = WeakValueDictionary()
STATIONS = WeakValueDictionary()

def get_constellation(constellation_id):
    """Retrieves or populates the requested constellation"""
    from model.static.map.constellation import Constellation
    if constellation_id not in CONSTELLATIONS:
        constellation = Constellation(constellation_id)
        CONSTELLATIONS[constellation_id] = constellation 
    return CONSTELLATIONS[constellation_id]

def get_region(region_id):
    """Retrieves or populates the requested region"""
    from model.static.map.region import Region
    if region_id not in REGIONS:
        region = Region(region_id)
        REGIONS[region_id] = region
    return REGIONS[region_id]

def get_solar_system(solar_system_id):
    """Retrieves or populates the requested solar system"""
    from model.static.map.solar_system import SolarSystem
    if solar_system_id not in SOLAR_SYSTEMS:
        solar_system = SolarSystem(solar_system_id)
        SOLAR_SYSTEMS[solar_system_id] = solar_system
    return SOLAR_SYSTEMS[solar_system_id]
    
def get_station(station_id):
    """Retrieves or populates the requested station"""
    from model.static.sta.station import Station
    if station_id not in STATIONS:
        station = Station(station_id)
        STATIONS[station_id] = station
    return STATIONS[station_id]