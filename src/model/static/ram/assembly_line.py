from model.flyweight import Flyweight
from model.static.database import database

class AssemblyLine(Flyweight):
    def __init__(self,assembly_line_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.assembly_line_id = assembly_line_id

        cursor = database.get_cursor(
            "select * from ramAssemblyLines where assemblyLineID={};".format(
                self.assembly_line_id))
        row = cursor.fetchone()

        self.assembly_line_type_id = row["assemblyLineTypeID"]
        self.container_id = row["containerID"]
        self.next_free_time = row["nextFreeTime"]
        self.ui_grouping_id = row["UIGroupingID"]
        self.cost_install = row["costInstall"]
        self.cost_per_hour = row["costPerHour"]
        self.restriction_mask = row["restrictionMask"]
        self.discount_per_good_standing_point = row["discountPerGoodStandingPoint"]
        self.surcharge_per_bad_standing_point = row["surchargePerBadStandingPoint"]
        self.minimum_standing = row["minimumStanding"]
        self.minimum_char_security = row["minimumCharSecurity"]
        self.minimum_corp_security = row["minimumCorpSecurity"]
        self.maximum_char_security = row["maximumCharSecurity"]
        self.maximum_corp_security = row["maximumCorpSecurity"]
        self.owner_id = row["ownerID"]
        self.activity_id = row["activityID"]

        cursor.close()
