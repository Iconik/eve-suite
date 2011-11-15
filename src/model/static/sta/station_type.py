from model.flyweight import Flyweight
from model.static.database import database

class StationType(Flyweight):
    def __init__(self,station_type_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.station_type_id = station_type_id

        cursor = database.get_cursor(
            "select * from staStationTypes where stationTypeID={};".format(
                self.station_type_id))
        row = cursor.fetchone()

        self.dock_entry_x = row["dockEntryX"]
        self.dock_entry_y = row["dockEntryY"]
        self.dock_entry_z = row["dockEntryZ"]
        self.dock_orientation_x = row["dockOrientationX"]
        self.dock_orientation_y = row["dockOrientationY"]
        self.dock_orientation_z = row["dockOrientationZ"]
        self.operation_id = row["operationID"]
        self.office_slots = row["officeSlots"]
        self.reprocessing_efficiency = row["reprocessingEfficiency"]
        self.conquerable = True if row["conquerable"] == 1 else False

        cursor.close()
