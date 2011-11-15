from model.static.database import database
from model.dynamic.inventory.item import Item
from model.flyweight import Flyweight

class TypeMaterials(Flyweight): #IGNORE:R0903
    """
    Data-class for the _materials needed for manufacturing, and returned by
    refining

    WARNING: The _materials herein, does include the recycled _materials for any
    T1 component in a T2 production.
    """

    def __init__(self, type_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.type_id = type_id
        self._materials = dict()
        cursor = database.get_cursor(
            "select * from invTypeMaterials where typeID={};".format(
                self.type_id))

        for row in cursor:
            self._materials[row["materialTypeID"]] = Item(row["materialTypeID"],
                quantity=row["quantity"])

        cursor.close()

    def values(self):
        return self._materials.values()

    def __getitem__(self, k):
        """Allows TypeMaterials[k]"""
        return self._materials[k]

    def __contains__(self, item):
        """Allows 'if item in TypeMaterials'"""
        return item in self._materials
