from model.flyweight import Flyweight
from model.static.database import database

class Activity(Flyweight):
    def __init__(self,activity_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.activity_id = activity_id

        cursor = database.get_cursor("select * from crpActivities where \
        activityID=%s;" % (self.activity_id))
        row = cursor.fetchone()

        self.activity_name = row["activityName"]
        self.description = row["description"]

        cursor.close()
