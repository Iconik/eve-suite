from collections import namedtuple
from model.flyweight import Flyweight
from model.static.database import database

class NPCCorporationTrade(Flyweight):
    def __init__(self,corporation_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing

        self.corporation_id = corporation_id

        cursor = database.get_cursor("select * from crpNPCCorporationTrades where \
        corporationID=%s;" % (self.corporation_id))

        self.trades = list()

        for row in cursor:
            self.trades.append(row["typeID"])

        cursor.close()
        
        self._trade_types = None
        
    def get_trade_types(self):
        if self._trade_types is None:
            from model.static.inv.type import Type
            self._trade_types = list()
            for item in self.trades:
                self._trade_types.append(Type(item))
        return self._trade_types