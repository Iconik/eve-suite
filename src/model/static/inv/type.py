from model.flyweight import Flyweight
from model.static.database import database

class Type(Flyweight):
    def __init__(self, type_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.type_id = type_id

        cursor = database.get_cursor(
            "select * from invTypes where typeID=%s;" % self.type_id)
        row = cursor.fetchone()

        self.type_name = row["typeName"]
        self.group_id = row["groupID"]
        self.description = row["description"]
        self.graphic_id = row["graphicID"]
        self.radius = row["radius"]
        self.mass = row["mass"]
        self.volume = row["volume"]
        self.capacity = row["capacity"]
        self.portion_size = row["portionSize"]
        self.race_id = row["raceID"]
        self.base_price = row["basePrice"]
        self.published = True if row["published"] == 1 else False
        self.market_group_id = row["marketGroupID"]
        self.chance_of_duplicating = row["chanceOfDuplicating"]

        cursor.close()

        self._group = None
        self._market_group = None
        self._attributes = None
        self._materials = None
        self._manufacturable = None
        self._blueprint = None
        self._blueprint_type_id = None

    def get_group(self):
        """Populates and returns the _group"""
        if self._group is None:
            from model.static.inv.group import Group
            self._group = Group(self.group_id)
        return self._group

    def get_market_group(self):
        """Populates and returns the market _group"""
        if self._market_group is None:
            from model.static.inv.market_group import MarketGroup
            self._market_group = MarketGroup(self.market_group_id)
        return self._market_group

    def get_attributes(self):
        """Populates and returns the _attributes"""
        if self._attributes is None:
            from model.static.dgm.type_attributes import TypeAttributes
            self._attributes = TypeAttributes(self.type_id)
        return self._attributes

    def get_materials(self):
        """Populates and returns the _materials"""
        from model.static.inv.type_materials import TypeMaterials
        if self._materials is None:
            self._materials = TypeMaterials(self.type_id)
        return self._materials

    def is_manufacturable(self):
        """Returns true if the type can be manufactured, false if not, and also
        populates the blueprint_id"""

        if self._manufacturable is None:
            cursor = database.get_cursor(
                "select * from invBlueprintTypes where productTypeID=%s;" %
                self.type_id)
            #cursor.fetchall()
            row = cursor.fetchone()
            if row is not None:
                self._blueprint_type_id = row["blueprintTypeID"]
                self._manufacturable = True
            else:
                self._manufacturable = False
        return self._manufacturable

    def get_blueprint_type(self):
        """populates the _blueprint reference, if the type can be manufactured"""
        from model.static.inv.blueprint_type import BlueprintType
        if self._blueprint is None:
            if self.is_manufacturable():
                blue = BlueprintType(self._blueprint_type_id)
                self._blueprint = blue
        return self._blueprint
