'''
Created on 23 Dec 2009

@author: FrederikNS
'''
from model.static.database import database
from model.static.map import map_dictionaries
from model.static.character import character_dictionaries
from model.static.corporation import corporation_dictionaries

class Faction(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EH2kdREREd-LgJ4IxcJkTA
    """

    def __init__(self, faction_id):
        '''
        Constructor
        '''
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
            self.race = character_dictionaries.get_race(self.race_ids)
        return self.race
    
    
    def get_solar_system(self):
        """Populates and returns the solar system"""
        if self.solar_system is None:
            self.solar_system = \
            map_dictionaries.get_solar_system(self.solar_system_id)
        return self.solar_system
    
    def get_corporation(self):
        """Populates and returns the corporation"""
        if self.corporation is None:
            self.corporation = \
            corporation_dictionaries.get_npc_corporation(self.corporation_id)
        return self.corporation
    
    
    def get_militia_corporation(self):
        """Populates and returns the militia corporation"""
        if self.militia_corporation is None:
            self.militia_corporation = \
            corporation_dictionaries.get_npc_corporation \
            (self.militia_corporation_id)
        return self.militia_corporation
    
