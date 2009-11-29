'''
Created on Nov 26, 2009

@author: frederikns
'''
from Model.Universe.Constellation import Constellation
from Model.Universe.Region import Region
from Model.Universe.SolarSystem import SolarSystem
from Model.Universe.Station import Station
from weakref import WeakValueDictionary

class UniverseDictionaries(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.constellations = WeakValueDictionary()
        self.regions = WeakValueDictionary()
        self.solarSystems = WeakValueDictionary()
        self.stations = WeakValueDictionary()
        
    def get_constellation(self,constellationID):
        if constellationID not in self.constellations:
            constellation = Constellation(constellationID)
            self.constellations[constellationID] = constellation 
        return self.constellations[constellationID]
    
    def get_region(self,regionID):
        if regionID not in self.regions:
            region = Region(regionID)
            self.regions[regionID] = region
        return self.regions[regionID]
    
    def get_solarSystem(self,solarSystemID):
        if solarSystemID not in self.solarSystems:
            solarSystem = SolarSystem(solarSystemID)
            self.solarSystems[solarSystemID] = solarSystem
        return self.solarSystems[solarSystemID]
    
    def get_station(self,stationID):
        if stationID not in self.stations:
            station = Station(stationID)
            self.stations[stationID] = station
        return self.stations[stationID]