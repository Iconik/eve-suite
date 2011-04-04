from model.flyweight import Flyweight
from model.static.database import database

class Bloodline(Flyweight):
    def __init__(self,bloodline_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.bloodline_id = bloodline_id

        cursor = database.get_cursor("select * from chrBloodlines where \
        bloodlineID=%s;" % (self.bloodline_id))
        row = cursor.fetchone()

        self.bloodline_name = row["bloodlineName"]
        self.race_id = row["raceID"]
        self.description = row["description"]
        self.male_description = row["maleDescription"]
        self.female_description = row["femaleDescription"]
        self.ship_type_id = row["shipTypeID"]
        self.corporation_id = row["corporationID"]
        self.perception = row["perception"]
        self.willpower = row["willpower"]
        self.charisma = row["charisma"]
        self.memory = row["memory"]
        self.intelligence = row["intelligence"]
        self.icon_id = row["iconID"]
        self.short_description = row["shortDescription"]
        self.short_male_description = row["shortMaleDescription"]
        self.short_female_description = row["shortFemaleDescription"]

        cursor.close()
