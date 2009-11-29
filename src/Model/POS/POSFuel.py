'''
Created on Nov 15, 2009

@author: frederikns
'''
from Model.Inventory.Item import Item
import sqlite3

class POSFuel(object):
    '''
    classdocs
    '''

    def __init__(self,id):
        '''
        Constructor
        '''
        conn = sqlite3.connect('../../../Resources/Database/apo15-sqlite3-v1.db')
        cur = conn.cursor()
        cur.execute("select * from invControlTowerResources where controlTowerTypeID='%s';" % (id))
        
        self.online = list()
        self.power = list()
        self.cpu = list()
        self.reinforce = list()
        for row in cur:
            if row[2]==1:
                self.online.append((Item(row[1],quantity=row[3]),row[4],row[5]))
            elif row[2]==2:
                self.power.append((Item(row[1],quantity=row[3]),row[4],row[5]))
            elif row[2]==3:
                self.cpu.append((Item(row[1],quantity=row[3]),row[4],row[5]))
            elif row[2]==4:
                self.reinforce.append((Item(row[1],quantity=row[3]),row[4],row[5]))
                
    def get_online(self):
        return self.online
    def get_power(self):
        return self.power
    def get_cpu(self):
        return self.cpu
    def get_reinforce(self):
        return self.reinforce