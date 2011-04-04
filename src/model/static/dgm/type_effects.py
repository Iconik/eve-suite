from model.flyweight import Flyweight
from model.static.database import database
from collections import namedtuple

class TypeEffects(Flyweight):
    def __init__(self,type_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.type_id = type_id

        cursor = database.get_cursor("select * from dgmTypeEffects where \
        typeID=%s;" % (self.type_id))
        
        self.effects = list()
        
        effect = namedtuple("effect", "effect_id is_default")
        
        for row in cursor:
            self.effects.append(effect(effect_id=row["effectID"], is_default=True if row["isDefault"] == 1 else False))

        cursor.close()
