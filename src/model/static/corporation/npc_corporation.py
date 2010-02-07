'''
Created on 23 Dec 2009

@author: FrederikNS
'''
from model.static.database import database
from model.static.map import map_dictionaries
from model.static.corporation import corporation_dictionaries

class NPCCorporation(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EH5nxxEREd-LgJ4IxcJkTA
    """

    def __init__(self, corporation_id):
        self.corporation_id = corporation_id
        
        cursor = database.get_cursor("select * from crpNPCCorporations where \
        corporationID=%s" % (self.corporation_id))
        row = cursor.fetchone()
        
        self.size = row["size"]
        self.extent = row["extent"]
        self.solar_system_id = row["solarSystemID"]
        self.investor_ids = [row["investorID1"], row["investorID2"],
                             row["investorID3"], row["investorID4"]]
        self.investor_shares = [row["investorShares1"], row["investorShares2"],
                                row["investorShares3"], row["investorShares4"]]
        self.friend_id = row["friendID"]
        self.enemy_id = row["enemyID"]
        self.public_shares = row["publicShares"]
        self.initial_price = row["initialPrice"]
        self.min_security = row["minSecurity"]
        self.scattered = row["scattered"]
        self.fringe = row["fringe"]
        self.corridor = row["corridor"]
        self.hub = row["hub"]
        self.border = row["border"]
        self.faction_id = row["factionID"]
        self.size_factor = row["sizeFactor"]
        self.station_count = row["stationCount"]
        self.station_system_count = row["stationSystemCount"]
        self.description = row["description"]
        
        cursor.close()
        
        self.solar_system = None
        self.investors = None
        self.friend = None
        self.enemy = None
        
    def get_solar_system(self):
        """Populates and returns the solar system"""
        if self.solar_system is None:
            self.solar_system = map_dictionaries.get_solar_system \
            (self.solar_system_id)
        return self.solar_system
    
    def get_investor(self, investor_index):
        """Populates and returns the requested investor"""
        if self.investors is None:
            self.investors = list()
        if self.investors[investor_index] is None:
            self.investors[investor_index] = corporation_dictionaries.\
            get_npc_corporation(self.investor_ids[investor_index])
        return self.investors[investor_index]
    
    def get_friend(self):
        """Populates and returns the friend"""
        if self.friend is None:
            self.friend = corporation_dictionaries.\
            get_npc_corporation(self.friend_id)
        return self.friend
    
    def get_enemy(self):
        """Populates and returns the enemy"""
        if self.enemy is None:
            self.enemy = corporation_dictionaries.\
            get_npc_corporation(self.enemy_id)
        return self.enemy
