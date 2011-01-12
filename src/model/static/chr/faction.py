'''
Created on 23 Dec 2009

@author: FrederikNS
'''
from model.flyweight import Flyweight
from model.static.database import database

class Faction(Flyweight):
    def __init__(self, faction_id):
        #prevents reinitializing
        if "inited" in self.__dict__:
            return
        self.inited = None
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
        
        self.race = None
        self.solar_system = None
        self.corporation = None
        self.militia_corporation = None
        
    def get_race(self):
        """Populates and returns the race"""
        if self.race is None:
            from model.static.chr.race import Race
            self.race = Race(self.race_ids)
        return self.race
    
    def get_solar_system(self):
        """Populates and returns the solar system"""
        if self.solar_system is None:
            from model.static.map.solar_system import SolarSystem
            self.solar_system = SolarSystem(self.solar_system_id)
        return self.solar_system
    
    def get_corporation(self):
        """Populates and returns the corporation"""
        if self.corporation is None:
            from model.static.crp.npc_corporation import NPCCorporation
            self.corporation = NPCCorporation(self.corporation_id)
        return self.corporation
    
    
    def get_militia_corporation(self):
        """Populates and returns the militia corporation"""
        if self.militia_corporation is None:
            from model.static.crp.npc_corporation import NPCCorporation
            self.militia_corporation = NPCCorporation(
                self.militia_corporation_id)
        return self.militia_corporation
    
