from model.flyweight import Flyweight
from model.static.database import database
from collections import namedtuple

class ContrabandType(Flyweight):
    def __init__(self,faction_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.faction_id = faction_id

        cursor = database.get_cursor("select * from invContrabandTypes where \
        factionID=%s;" % (self.faction_id))
        
        self.contraband = list()
        
        contraband_tuple = namedtuple("contraband_tuple", "type_id standing_loss confiscate_min_sec fine_by_value attack_min_sec")
        
        for row in cursor:
            self.contraband.append(contraband_tuple(
                type_id = row["typeID"],
                standing_loss = row["standingLoss"],
                confiscate_min_sec = row["confiscateMinSec"],
                fine_by_value = row["fineByValue"],
                attack_min_sec = row["attackMinSec"]))

        cursor.close()
