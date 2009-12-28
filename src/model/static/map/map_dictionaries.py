'''
Created on Nov 26, 2009

@author: frederikns
'''
from weakref import WeakValueDictionary

constellations = WeakValueDictionary()
regions = WeakValueDictionary()
solar_systems = WeakValueDictionary()
stations = WeakValueDictionary()

def get_constellation(constellationID):
    from model.static.map.constellation import Constellation
    if constellationID not in constellations:
        constellation = Constellation(constellationID)
        constellations[constellationID] = constellation 
    return constellations[constellationID]

def get_region(regionID):
    from model.static.map.region import Region
    if regionID not in regions:
        region = Region(regionID)
        regions[regionID] = region
    return regions[regionID]

def get_solar_system(solarSystemID):
    from model.static.map.solar_system import SolarSystem
    if solarSystemID not in solar_systems:
        solar_system = SolarSystem(solarSystemID)
        solar_systems[solarSystemID] = solar_system
    return solar_systems[solarSystemID]
    
def get_station(stationID):
    from model.static.station.station import Station
    if stationID not in stations:
        station = Station(stationID)
        stations[stationID] = station
    return stations[stationID]