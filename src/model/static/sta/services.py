from model.flyweight import Flyweight
from model.static.database import database

class Service(Flyweight):
    def __init__(self,service_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.service_id = service_id

        cursor = database.get_cursor(
            "select * from staServices where serviceID={};".format(
                self.service_id))
        row = cursor.fetchone()

        self.service_name = row["serviceName"]
        self.description = row["description"]

        cursor.close()
