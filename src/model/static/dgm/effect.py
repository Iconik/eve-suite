from model.flyweight import Flyweight
from model.static.database import database

class Effect(Flyweight):
    def __init__(self,effect_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.effect_id = effect_id

        cursor = database.get_cursor("select * from dgmEffects where \
        effectID=%s;" % (self.effect_id))
        row = cursor.fetchone()

        self.effect_name = row["effectName"]
        self.effect_category = row["effectCategory"]
        self.pre_expression = row["preExpression"]
        self.post_expression = row["postExpression"]
        self.description = row["description"]
        self.guid = row["guid"]
        self.icon_id = row["iconID"]
        self.is_offensive = True if row["isOffensive"] == 1 else False
        self.is_assistance = True if row["isAssistance"] == 1 else False
        self.duration_attribute_id = row["durationAttributeID"]
        self.tracking_speed_attribute_id = row["trackingSpeedAttributeID"]
        self.discharge_attribute_id = row["dischargeAttributeID"]
        self.range_attribute_id = row["rangeAttributeID"]
        self.falloff_attribute_id = row["falloffAttributeID"]
        self.disallow_auto_repeat = True if row["disallowAutoRepeat"] == 1 else False
        self.published = True if row["published"] == 1 else False
        self.display_name = row["displayName"]
        self.is_warp_safe = True if row["isWarpSafe"] == 1 else False
        self.range_chance = True if row["rangeChance"] == 1 else False
        self.electronic_chance = True if row["electronicChance"] == 1 else False
        self.propulsion_chance = True if row["propulsionChance"] == 1 else False
        self.distribution = row["distribution"]
        self.sfx_name = row["sfxName"]
        self.npc_usage_chance_attribute_id = row["npcUsageChanceAttributeID"]
        self.npc_activation_chance_attribute_id = row["npcActivationChanceAttributeID"]
        self.fitting_usage_chance_attribute_id = row["fittingUsageChanceAttributeID"]

        cursor.close()
