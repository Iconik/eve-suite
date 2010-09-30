'''
Created on Nov 15, 2009

@author: frederikns
'''
from model.dynamic.inventory.item import Item
from model.static.database import database

class POSFuel(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EIPmABEREd-LgJ4IxcJkTA
    """

    def __init__(self, pos_type_id):
        '''
        Constructor
        '''
        cursor = database.get_cursor("select * from invControlTowerResources \
        where controlTowerTypeID='%s';" % (pos_type_id))
        
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
