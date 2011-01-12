'''
Created on Oct 28, 2009

@author: frederikns
'''
from model.static.database import database
from model.static.dgm.type_attributes import TypeAttributes
from model.flyweight import Flyweight
from model.static.inv.group import Group
from model.static.inv.market_group import MarketGroup
from model.static.inv.type_materials import TypeMaterials
from model.static.inv.blueprint_type import BlueprintType

class Type(Flyweight):
    def __init__(self, type_id):
        #prevents reinitializing
        if "inited" in self.__dict__:
            return
        self.inited = None
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
        self.published = row["published"]
        self.market_group_id = row["marketGroupID"]
        self.chance_of_duplicating = row["chanceOfDuplicating"]
        
        cursor.close()
    
        self.group = None
        self.market_group = None
        self.attributes = None
        self.materials = None
        self.manufacturable = None
        self.blueprint = None
        self.blueprint_type_id = None
        
    def get_group(self):
        """Populates and returns the group"""
        if self.group is None:
            self.group = Group(self.group_id)
        return self.group
    
    def get_market_group(self):
        """Populates and returns the market group"""
        if self.market_group is None:
            self.market_group = MarketGroup(self.market_group_id)
        return self.market_group
    
    def get_attributes(self):
        """Populates and returns the attributes"""
        if self.attributes is None:
            self.attributes = TypeAttributes(self.type_id)
        return self.attributes

    def get_materials(self):
        """Populates and returns the materials"""
        if self.materials is None:
            self.materials = TypeMaterials(self.type_id)
        return self.materials
    
    def is_manufacturable(self):
        """Returns true if the type can be manufactured, false if not, and also
        populates the blueprint_id"""
           
        if self.manufacturable is None:
            cursor = database.get_cursor(
                "select * from invBlueprintTypes where productTypeID=%s;" %
                self.type_id)
            if len(cursor) > 0:
                self.blueprint_type_id = cursor.fetchone()["blueprintTypeID"]
                self.manufacturable = True
            else:
                self.manufacturable = False
        return self.manufacturable
        
    def get_blueprint_type(self):
        """populates the blueprint reference, if the type can be manufactured"""
        if self.is_manufacturable():
            if self.blueprint is None:
                self.blueprint = BlueprintType(self.blueprint_type_id)
        return self.blueprint
        