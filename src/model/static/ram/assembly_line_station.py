from collections import namedtuple
from model.flyweight import Flyweight
from model.static.database import database

class AssemblyLineStation(Flyweight):
    def __init__(self,station_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.station_id = station_id

        cursor = database.get_cursor(
            "select * from ramAssemblyLineStations where stationID={};".format(
                self.station_id))

        self.assembly_lines = list()

        assembly_line_tuple = namedtuple("assembly_line_tuple", "assembly_line_type_id quantity station_type_id owner_id solar_system_id region_id ")

        for row in cursor:
            self.assembly_lines.append(assembly_line_tuple(
                assembly_line_type_id=row["assemblyLineTypeID"],
                quantity=row["quantity"],
                station_type_id=row["stationTypeID"],
                owner_id=row["ownerID"],
                solar_system_id=row["solarSystemID"],
                region_id=row["regionID"],
            ))

        cursor.close()
