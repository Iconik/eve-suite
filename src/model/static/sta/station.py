from model.static.database import database
from model.flyweight import Flyweight

class Station(Flyweight):
    def __init__(self, station_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.station_id = station_id

        cursor = database.get_cursor(
            "select * from staStations where stationID={};".format(
                self.station_id))
        row = cursor.fetchone()

        self.security = row["security"]
        self.docking_cost_per_volume = row["dockingCostPervolume"]
        self.max_ship_volume_dockable = row["maxShipVolumeDockable"]
        self.office_rental_cost = row["officeRentalCost"]
        self.operation_id = row["operationID"]
        self.station_type_id = row["stationTypeID"]
        self.corporation_id = row["corporationID"]
        self.solar_system_id = row["solarSystemID"]
        self.constellation_id = row["constellationID"]
        self.region_id = row["regionID"]
        self.station_name = row["stationName"]
        self.x_pos = row["x"]
        self.y_pos = row["y"]
        self.z_pos = row["z"]
        self.reprocessing_efficiency = row["reprocessingEfficiency"]
        self.reprocessing_stations_take = row["reprocessingStationsTake"]
        self.reprocessing_hangar_flag = row["reprocessingHangarFlag"]

        cursor.close()

        self._solar_system = None
        self._region = None
        self._constellation = None
        self._station_type = None

    def get_solar_system(self):
        """Populations and returns the solar system"""
        if self._solar_system is None:
            from model.static.map.solar_system import SolarSystem
            self._solar_system = SolarSystem(self.solar_system_id)
        return self._solar_system

    def get_region(self):
        """Populations and returns the _region"""
        if self._region is None:
            from model.static.map.region import Region
            self._region = Region(self.region_id)
        return self._region

    def get_constellation(self):
        """Populations and returns the _constellation"""
        if self._constellation is None:
            from model.static.map.constellation import Constellation
            self._constellation = Constellation(self.constellation_id)
        return self._constellation

    def get_stations_type(self):
        """Populations and returns the station type"""
        if self._station_type is None:
            from model.static.inv.type import Type
            self._station_type = Type(self.station_type_id)
        return self._station_type
