from model.flyweight import Flyweight
from model.static.database import database

class SolarSystem(Flyweight):
    def __init__(self, solar_system_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.solar_system_id = solar_system_id

        cursor = database.get_cursor("select * from mapSolarSystems where \
        solarSystemID=%s;" % (self.solar_system_id))
        row = cursor.fetchone()

        self.region_id = row["regionID"]
        self.constellation_id = row["constellationID"]
        self.solar_system_name = row["solarSystemName"]
        self.x_pos = row["x"]
        self.y_pos = row["y"]
        self.z_pos = row["z"]
        self.x_min = row["xMin"]
        self.x_max = row["xMax"]
        self.y_min = row["yMin"]
        self.y_ax = row["yMax"]
        self.z_min = row["zMin"]
        self.z_max = row["zMax"]
        self.luminosity = row["luminosity"]
        self.border = row["border"]
        self.fringe = row["fringe"]
        self.corridor = row["corridor"]
        self.hub = row["hub"]
        self.international = row["international"]
        self.regional = row["regional"]
        self._constellation = row["_constellation"]
        self.security = row["security"]
        self.faction_id = row["factionID"]
        self.radius = row["radius"]
        self.sun_type_id = row["sunTypeID"]
        self.security_class = row["securityClass"]

        cursor.close()

        self._region = None
        self._constellation = None
        self._sun_type = None

    def get_region(self):
        """Populates and returns the _region"""
        if self._region is None:
            from model.static.map.region import Region
            self._region = Region(self.region_id)
        return self._region

    def get_constellation(self):
        """Populates and returns the _constellation"""
        if self._constellation is None:
            from model.static.map.constellation import Constellation
            self._constellation = Constellation(self.constellation_id)
        return self._constellation

    def get_sun_type(self):
        """Populates and returns the sun type"""
        if self._sun_type is None:
            from model.static.inv.type import Type
            self._sun_type = Type(self.sun_type_id)
        return self._sun_type

    def __str__(self):
        return self.solar_system_name
