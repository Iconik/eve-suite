from model.flyweight import Flyweight
from model.static.database import database

class Denormalize(Flyweight):
    def __init__(self,item_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.item_id = item_id

        cursor = database.get_cursor("select * from mapDenormalize where \
        itemID=%s;" % (self.item_id))
        row = cursor.fetchone()

        self.type_id = row["typeID"]
        self.group_id = row["groupID"]
        self.solar_system_id = row["solarSystemID"]
        self.constellation_id = row["constellationID"]
        self.region_id = row["regionID"]
        self.orbit_id = row["orbitID"]
        self.x = row["x"]
        self.y = row["y"]
        self.z = row["z"]
        self.radius = row["radius"]
        self.item_name = row["itemName"]
        self.security = row["security"]
        self.celestial_index = row["celestialIndex"]
        self.orbit_index = row["orbitIndex"]

        cursor.close()

        self._type = None
        self._group = None
        self._solar_system = None
        self._constellation = None
        self._region = None
        self._orbit = None

    def get_type(self):
        if self._type is None:
            from model.static.inv.type import Type
            self._type = Type(self.type_id)
        return self._type

    def get_group(self):
        if self._group is None:
            from model.static.inv.group import Group
            self._group = Group(self.group_id)
        return self._group

    def get_solar_system(self):
        if self._solar_system is None:
            from model.static.map.solar_system import SolarSystem
            self._solar_system = SolarSystem(self.solar_system_id)
        return self._solar_system

    def get_constellation(self):
        if self._constellation is None:
            from model.static.map.constellation import Constellation
            self._constellation = Constellation(self.constellation_id)
        return self._constellation

    def get_region(self):
        if self._region is None:
            from model.static.map.region import Region
            self._region = Region(self.region_id)
        return self._region
