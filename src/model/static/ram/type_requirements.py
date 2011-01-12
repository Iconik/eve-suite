'''
Created on 9 Feb 2010

@author: FrederikNS
'''
from collections import namedtuple

from model.flyweight import Flyweight
from model.static.database import database
from model.dynamic.inventory.item import Item

class TypeRequirements(Flyweight): #IGNORE:R0903
    def __init__(self, type_id):
        #prevents reinitializing
        if "inited" in self.__dict__:
            return
        self.inited = None
        #prevents reinitializing

        self.type_id = type_id
        
        """Remember: the key is the activity type
        0 = None
        1 = Manufacturing
        2 = Research Technology
        3 = Research Time Productivity
        4 = Research Material Productivity
        5 = Copying
        6 = Duplicating
        7 = Reverse Engineering
        8 = Invention"""
        self.requirements = dict()
        
        cursor = database.get_cursor("select * \
        from ramTypeRequirements where typeID=%s;" % (self.type_id))
        
        requirement = namedtuple("requirement", "item, damage, recycle")
        
        for row in cursor:
            if row["activityID"] not in self.requirements:
                self.requirements[row["activityID"]] = list()
            self.requirements[row["activityID"]].append(requirement(
                item=Item(row["requiredTypeID"], quantity=row["quantity"]),
                damage=row["damagePerJob"],
                recycle=True if row["recycle"] == 1 else False))
            
    def __getitem__(self, k):
        """Allows TypeRequirements[k]"""
        return self.requirements[k]