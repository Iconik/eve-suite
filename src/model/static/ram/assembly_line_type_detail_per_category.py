from collections import namedtuple
from model.flyweight import Flyweight
from model.static.database import database

class AssemblyLineTypeDetailPerCategory(Flyweight):
    def __init__(self,assembly_line_type_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.assembly_line_type_id = assembly_line_type_id

        cursor = database.get_cursor("select * from ramAssemblyLineTypeDetailPerCategory where \
        assemblyLineTypeID=%s;" % (self.assembly_line_type_id))

        self.categories = list()

        category_tuple = namedtuple("category_tuple", "category_id time_multiplier material_multiplier ")

        for row in cursor:
            self.categories.append(category_tuple(
                category_id=row["categoryID"],
                time_multiplier=row["timeMultiplier"],
                material_multiplier=row["materialMultiplier"],
            ))

        cursor.close()
