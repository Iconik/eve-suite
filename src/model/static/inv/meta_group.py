from model.flyweight import Flyweight
from model.static.database import database

class MetaGroup(Flyweight):
    def __init__(self,meta_group_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.meta_group_id = meta_group_id

        cursor = database.get_cursor(
            "select * from invMetaGroups where metaGroupID={};".format(
                self.meta_group_id))
        row = cursor.fetchone()

        self.meta_group_name = row["metaGroupName"]
        self.description = row["description"]
        self.icon_id = row["iconID"]

        cursor.close()
