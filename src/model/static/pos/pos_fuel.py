from model.flyweight import Flyweight
from model.static.database import database
from model.dynamic.inventory.item import Item

class POSFuel(Flyweight):
    def __init__(self, pos_type_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        cursor = database.get_cursor(
            "select * from invControlTowerResources where controlTowerTypeID={};".format(pos_type_id))

        self.online = list()
        self.power = list()
        self.cpu = list()
        self.reinforce = list()
        for row in cursor:
            if row["purpose"] == 1:
                self.online.append((Item(row["resourceTypeID"],
                                         quantity=row["quantity"]),
                                         row["minSecurityLevel"],
                                         row["factionID"]))
            elif row["purpose"] == 2:
                self.power.append((Item(row["resourceTypeID"],
                                        quantity=row["quantity"]),
                                        row["minSecurityLevel"],
                                        row["factionID"]))
            elif row["purpose"] == 3:
                self.cpu.append((Item(row["resourceTypeID"],
                                      quantity=row["quantity"]),
                                      row["minSecurityLevel"],
                                      row["factionID"]))
            elif row["purpose"] == 4:
                self.reinforce.append((Item(row["resourceTypeID"],
                                            quantity=row["quantity"]),
                                            row["minSecurityLevel"],
                                            row["factionID"]))

        cursor.close()
