from model.flyweight import Flyweight
from model.static.database import database

class TypeReaction(Flyweight):
    def __init__(self,reaction_type_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.reaction_type_id = reaction_type_id

        cursor = database.get_cursor(
            "select * from invTypeReactions where reactionTypeID={};".format(
                self.reaction_type_id))

        cursor.close()
