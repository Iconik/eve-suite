from model.flyweight import Flyweight
from model.static.database import database

class TranslationColumn(Flyweight):
    def __init__(self,tc_group_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.tc_group_id = tc_group_id

        cursor = database.get_cursor(
            "select * from trnTranslationColumns where tcGroupID={};".format(
                self.tc_group_id))
        row = cursor.fetchone()

        self.tc_id = row["tcID"]
        self.table_name = row["tableName"]
        self.column_name = row["columnName"]
        self.master_id = row["masterID"]

        cursor.close()
