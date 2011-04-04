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

        cursor = database.get_cursor("select * from ramActivities where \
        activityID=%s;" % (self.market_group_id))
        row = cursor.fetchone()

        self.activity_name = row["activityID"]
        self.icon_no = row["iconNo"]
        self.description = row["description"]
        self.published = True if row["published"] == 1 else False

        cursor.close()
