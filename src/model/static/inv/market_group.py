from model.static.database import database
from model.flyweight import Flyweight


class MarketGroup(Flyweight):
    def __init__(self, market_group_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing
        
        self.market_group_id = market_group_id
        cursor = database.get_cursor("select * from invMarketGroups where \
        marketGroupID=%s;" % (self.market_group_id))
        row = cursor.fetchone()
        
        self.parent_group_id = row["parentGroupID"]
        self.market_group_name = row["marketGroupName"]
        self.description = row["description"]
        self.graphics_id = row["graphicsID"]
        self.has_types = row["hasTypes"]
        
        cursor.close()
        
        self._parent_group = None
        
    def get_parent_group(self):
        """Populates and returns the parent group"""
        if self._parent_group is None:
            from model.static.inv.group import Group
            self._parent_group = Group(self.parent_group_id)
        return self._parent_group
