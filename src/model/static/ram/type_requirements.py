'''
Created on 9 Feb 2010

@author: FrederikNS
'''
from model.static.database import database
from model.dynamic.inventory.item import Item

class TypeRequirements(object):
    '''
    classdocs
    '''

    def __init__(self,type_id):
        '''
        Constructor
        '''
        
        self.type_id = type_id
        
        self.requirements = dict()
        
        cursor = database.get_cursor("select * \
        from ramTypeRequirements where typeID=%s;" % (self.type_id))
        
        for row in cursor:
            if row["activityID"] not in self.requirements:
                self.requirements[row["activityID"]] = list()
            self.requirements[row["activityID"]].append((Item(row["requiredTypeID"], quantity=row["quantity"]), row["damagePerJob"], row["recycle"]))

