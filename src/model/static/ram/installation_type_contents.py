from collections import namedtuple
from model.flyweight import Flyweight
from model.static.database import database

class InstallationTypeContent(Flyweight):
    def __init__(self,installation_type_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.installation_type_id = installation_type_id

        cursor = database.get_cursor(
            "select * from ramInstallationTypeContents where installationTypeID={};".format(self.installation_type_id))

        self.assembly_lines = list()

        assembly_line_tuple = namedtuple("assembly_line_tuple", "assembly_line_type_id quantity ")

        for row in cursor:
            self.assembly_lines.append(assembly_line_tuple(
                assembly_line_type_id=row["assemblyLineTypeID"],
                quantity=row["quantity"],
            ))

        cursor.close()
