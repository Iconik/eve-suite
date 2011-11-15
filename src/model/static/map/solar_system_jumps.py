from collections import namedtuple
from model.flyweight import Flyweight
from model.static.database import database

class SolarSystemJump(Flyweight):
    def __init__(self,from_solar_system_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.from_solar_system_id = from_solar_system_id

        cursor = database.get_cursor(
            "select * from mapSolarSystemJumps where fromSolarSystemID={};".format(self.from_solar_system_id))

        self.YYY = list()

        XXX = namedtuple("XXX", "from_region_id from_constellation_id to_solar_system_id to_constellation_id to_region_id ")

        for row in cursor:
            self.YYY.append(XXX(
                from_region_id=row["fromRegionID"],
                from_constellation_id=row["fromConstellationID"],
                to_solar_system_id=row["toSolarSystemID"],
                to_constellation_id=row["toConstellationID"],
                to_region_id=row["toRegionID"],
            ))

        cursor.close()
