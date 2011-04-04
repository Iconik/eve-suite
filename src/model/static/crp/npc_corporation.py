from model.flyweight import Flyweight
from model.static.database import database
import weakref

class NPCCorporation(Flyweight):
    def __init__(self,corporation_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.corporation_id = corporation_id

        cursor = database.get_cursor("select * from crpNPCCorporations where \
        corporationID=%s;" % (self.corporation_id))
        row = cursor.fetchone()

        self.size = row["size"]
        self.extent = row["extent"]
        self.solar_system_id = row["solarSystemID"]
        self.investor_id1 = row["investorID1"]
        self.investor_ids = (row["investorID1"], row["investorID2"],
            row["investorID3"], row["investorID4"])
        self.investor_shares = (row["investorShares1"], row["investorShares2"],
            row["investorShares3"], row["investorShares4"])
        self.friend_id = row["friendID"]
        self.enemy_id = row["enemyID"]
        self.public_shares = row["publicShares"]
        self.initial_price = row["initialPrice"]
        self.min_security = row["minSecurity"]
        self.scattered = True if row["scattered"] == 1 else False
        self.fringe = row["fringe"]
        self.corridor = row["corridor"]
        self.hub = row["hub"]
        self.border = row["border"]
        self.faction_id = row["factionID"]
        self.size_factor = row["sizeFactor"]
        self.station_count = row["stationCount"]
        self.station_system_count = row["stationSystemCount"]
        self.description = row["description"]
        self.icon_id = row["iconID"]

        cursor.close()

        self._solar_system = None
        self._investors = None
        self._friend = None
        self._enemy = None
        self._faction = None

    def get_solar_system(self):
        """Populates and returns the solar system"""
        if self._solar_system is None:
            from model.static.map.solar_system import SolarSystem
            self._solar_system = SolarSystem(self.solar_system_id)
        return self._solar_system

    def get_investor(self, investor_index):
        """Populates and returns the requested investor"""
        if self._investors is None:
            self._investors = weakref.WeakValueDictionary()
        if investor_index not in self._investors:
            investor = self._investors[investor_index] = NPCCorporation(
                self.investor_ids[investor_index])
            return investor
        return self._investors[investor_index]

    def get_friend(self):
        """Populates and returns the _friend"""
        if self._friend is None:
            self._friend = weakref.ref(NPCCorporation(self.friend_id))
        return self._friend

    def get_enemy(self):
        """Populates and returns the _enemy"""
        if self._enemy is None:
            self._enemy = NPCCorporation(self.enemy_id)
        return self._enemy

    def get_faction(self):
        if self._faction is None:
            from model.static.chr.faction import Faction
            self._faction = Faction(self.faction_id)
        return self._faction