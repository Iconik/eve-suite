from model.flyweight import Flyweight
from model.static.database import database

class AssemblyLineType(Flyweight):
    def __init__(self,assembly_line_type_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.assembly_line_type_id = assembly_line_type_id

        cursor = database.get_cursor(
            "select * from ramAssemblyLineTypes where assemblyLineTypeID={};".format(self.assembly_line_type_id))
        row = cursor.fetchone()

        self.assembly_line_type_name = row["assemblyLineTypeName"]
        self.description = row["description"]
        self.base_time_multiplier = row["baseTimeMultiplier"]
        self.base_material_multiplier = row["baseMaterialMultiplier"]
        self.volume = row["volume"]
        self.activity_id = row["activityID"]
        self.min_cost_per_hour = row["minCostPerHour"]

        cursor.close()
