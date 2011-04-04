from collections import namedtuple
from model.flyweight import Flyweight
from model.static.database import database

class ConstellationJumps(Flyweight):
    def __init__(self,from_constellation_id):
        """TODO: Verify that this class works as intended"""
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.from_constellation_id = from_constellation_id

        cursor = database.get_cursor("select * from mapConstellationJumps where \
        fromConstellationID=%s;" % (self.from_constellation_id))

        self.jumps = list()

        jump_tuple = namedtuple("jump_tuple", "from_region_id to_constellation_id to_region_id ")

        for row in cursor:
            self.jumps.append(jump_tuple(
                from_region_id=row["fromRegionID"],
                to_constellation_id=row["toConstellationID"],
                to_region_id=row["toRegionID"],
            ))

        cursor.close()
