from model.flyweight import Flyweight
from model.static.database import database

class Operation(Flyweight):
    def __init__(self,activity_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.activity_id = activity_id

        cursor = database.get_cursor(
            "select * from staOperations where activityID={};".format(
                self.activity_id))
        row = cursor.fetchone()

        self.operation_id = row["operationID"]
        self.operation_name = row["operationName"]
        self.description = row["description"]
        self.fringe = row["fringe"]
        self.corridor = row["corridor"]
        self.hub = row["hub"]
        self.border = row["border"]
        self.ratio = row["ratio"]
        self.caldari_station_type_id = row["caldariStationTypeID"]
        self.minmatar_station_type_id = row["minmatarStationTypeID"]
        self.amarr_station_type_id = row["amarrStationTypeID"]
        self.gallente_station_type_id = row["gallenteStationTypeID"]
        self.jove_station_type_id = row["joveStationTypeID"]

        cursor.close()
