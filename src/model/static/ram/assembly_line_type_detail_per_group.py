from collections import namedtuple
from model.flyweight import Flyweight
from model.static.database import database

class AssemblyLineTypeDetailPerGroup(Flyweight):
    def __init__(self,assembly_line_type_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.assembly_line_type_id = assembly_line_type_id

        cursor = database.get_cursor(
            "select * from ramAssemblyLineTypeDetailPerGroup where assemblyLineTypeID={};".format(self.assembly_line_type_id))

        self.groups = list()

        group_tuple = namedtuple("group_tuple", "group_id time_multiplier material_multiplier ")

        for row in cursor:
            self.groups.append(group_tuple(
                group_id=row["groupID"],
                time_multiplier=row["timeMultiplier"],
                material_multiplier=row["materialMultiplier"],
            ))

        cursor.close()
