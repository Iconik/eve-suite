from model.flyweight import Flyweight
from model.static.database import database

class MetaType(Flyweight):
    def __init__(self,type_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.type_id = type_id

        cursor = database.get_cursor(
            "select * from invMetaTypes where typeID={};".format(self.type_id))
        row = cursor.fetchone()

        self.parent_type_id = row["parentTypeID"]
        self.meta_group_id = row["metaGroupID"]

        cursor.close()
