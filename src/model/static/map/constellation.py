from model.flyweight import Flyweight
from model.static.database import database

class Constellation(Flyweight):
    def __init__(self, constellation_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing
        
        self.constellation_id = constellation_id
        
        cursor = database.get_cursor("select * from mapConstellations where \
        constellationID='%s';" % (self.constellation_id))
        row = cursor.fetchone()
        
        self.region_id = row["regionID"]
        self.constellation_name = row["constellationName"]
        self.x_pos = row["x"]
        self.y_pos = row["y"]
        self.z_pos = row["z"]
        self.x_min = row["xMin"]
        self.x_max = row["xMax"]
        self.y_min = row["yMin"]
        self.y_max = row["yMax"]
        self.z_min = row["zMin"]
        self.z_max = row["zMax"]
        self.faction_id = row["factionID"]
        self.radius = row["radius"]
        
        self._region = None
        self._faction = None
        
    def get_region(self):
        """Populates and returns the _region"""
        if self._region is None:
            from model.static.map.region import Region
            self._region = Region(self.region_id)
        return self._region
    
    def get_faction(self):
        """Populates and returns the _faction"""
        if self._faction is None:
            from model.static.chr.faction import Faction
            self._faction = Faction(self.faction_id)
        return self._faction
