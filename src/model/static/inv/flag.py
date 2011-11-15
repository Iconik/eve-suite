from model.flyweight import Flyweight
from model.static.database import database

class Flag(Flyweight):
    def __init__(self,flag_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.flag_id = flag_id

        cursor = database.get_cursor(
            "select * from invFlags where flagID={};".format(self.flag_id))
        row = cursor.fetchone()

        self.flag_name = row["flagName"]
        self.flag_text = row["flagText"]
        self.order_id = row["orderID"]

        cursor.close()
