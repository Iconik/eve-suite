from model.flyweight import Flyweight
from model.static.database import database

class RegionJumps(Flyweight):
    def __init__(self,from_region_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.from_region_id = from_region_id

        cursor = database.get_cursor(
            "select * from mapRegionJumps where fromRegionID={};".format(
                self.from_region_id))

        self.YYY = list()

        for row in cursor:
            self.YYY.append(row["toRegionID"])

        cursor.close()
