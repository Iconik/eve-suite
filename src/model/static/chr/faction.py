'''
Created on 23 Dec 2009

@author: FrederikNS
'''
from model.flyweight import Flyweight
from model.static.database import database

class Faction(Flyweight):
    def __init__(self, faction_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.faction_id = faction_id
        
        cursor = database.get_cursor("select * from chrFactions where \
        factionID=%s;" % (self.faction_id))
        row = cursor.fetchone()
        
        self.faction_name = row["factionName"]
        self.description = row["description"]
        self.race_ids = row["raceIDs"]
        self.solar_system_id = row["solarSystemID"]
        self.corporation_id = row["corporationID"]
        self.size_factor = row["sizeFactor"]
        self.station_count = row["stationCount"]
        self.station_system_count = row["stationSystemCount"]
        self.militia_corporation_id = row["militiaCorporationID"]
        
        self._race = None
        self._solar_system = None
        self._corporation = None
        self._militia_corporation = None
        
    def get_race(self):
        """Populates and returns the _race"""
        if self._race is None:
            from model.static.chr.race import Race
            self._race = Race(self.race_ids)
        return self._race
    
    def get_solar_system(self):
        """Populates and returns the solar system"""
        if self._solar_system is None:
            from model.static.map.solar_system import SolarSystem
            self._solar_system = SolarSystem(self.solar_system_id)
        return self._solar_system
    
    def get_corporation(self):
        """Populates and returns the _corporation"""
        if self._corporation is None:
            from model.static.crp.npc_corporation import NPCCorporation
            self._corporation = NPCCorporation(self.corporation_id)
        return self._corporation
    
    
    def get_militia_corporation(self):
        """Populates and returns the militia _corporation"""
        if self._militia_corporation is None:
            from model.static.crp.npc_corporation import NPCCorporation
            self._militia_corporation = NPCCorporation(
                self.militia_corporation_id)
        return self._militia_corporation
    
