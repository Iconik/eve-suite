'''
Created on 23 Dec 2009

@author: FrederikNS
'''
from model.static.database import database
from model.static.map import map_dictionaries
from model.static.character import character_dictionaries
from model.static.corporation import corporation_dictionaries

class Faction(object):
    '''
    classdocs
    '''

    def __init__(self,faction_id):
        '''
        Constructor
        '''
        self.faction_id = faction_id
        
        cursor = database.get_cursor("select * from chrFactions where factionID=%s;" % (self.faction_id))
        row = cursor.fetchone()
        
        self.faction_name = row["factionName"]
        self.description = row["description"]
        self.race_ids = row["raceIDs"]
        self.solar_system_id = row["solarSystemID"]
        self.corporation_id = row["corporationID"]
        self.size_factor = row["sizeFactor"]
        self.station_count = row["stationCount"]
        self.station_system_count["stationSystemCount"]
        self.militia_corporation_id["militiaCorporationID"]
        
    def get_race(self):
        if 'self.race' not in locals():
            self.race = character_dictionaries.get_race(self.race_ids)
        return self.race
    
    
    def get_solar_system(self):
        if 'self.solar_system' not in locals():
            self.solar_system = map_dictionaries.get_solar_system(self.solar_system_id)
        return self.solar_system
    
    def get_corporation(self):
        if 'self.corporation' not in locals():
            self.corporation = corporation_dictionaries.get_corporation(self.corporation_id)
        return self.corporation
    
    
    def get_militia_corporation(self):
        if 'self.militia_corporation' not in locals():
            self.militia_corporation = corporation_dictionaries.get_corporation(self.militia_corporation_id)
        return self.militia_corporation
    