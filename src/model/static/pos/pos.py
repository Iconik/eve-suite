'''
Created on Nov 15, 2009

@author: frederikns
'''
from model.static.inventory import inventory_dictionaries
from model.static.pos import pos_dictionaries

import datetime
import math

class POS(object):
    '''
    classdocs
    '''

    def __init__(self,type_id,power,cpu,faction):
        '''
        Constructor
        '''
        self.type_id = type_id
        self.power = power
        self.cpu = cpu
        self.faction = faction
        
        
    def get_type(self):
        if 'self.type' not in locals():
            self.type = inventory_dictionaries.get_type(self.id)
        return self.type
    
    def get_fuel(self):
        if 'self.fuel' not in locals():
            self.fuel = pos_dictionaries.get_pos_fuel(self.id)
        return self.fuel
    
    def max_fuel(self):
        online_volume=0.0
        power_volume=0.0
        cpu_volume=0.0
        
        for x in self.fuel.get_online():
            if x[2]==self.faction or x[2]==None:
                online_volume+=x[0].get_volume()
        
        for x in self.fuel.get_power():
            power_volume+=x[0].get_volume()
        power_volume*=self.power
        
        for x in self.fuel.get_cpu():
            cpu_volume+=x[0].get_volume()
        cpu_volume*=self.cpu
        
        total_volume=online_volume+power_volume+cpu_volume
        
        fuel_multiplier=self.type.get_capacity()/total_volume
        
        print("Tower: ",self.type.get_typeName())
        
        for x in self.fuel.get_online():
            if x[2]==self.faction or x[2]==None:
                print(math.trunc(x[0].get_quantity()*fuel_multiplier),"\t",x[0].get_type().get_typeName())
        for x in self.fuel.get_power():
            print(math.trunc(x[0].get_quantity()*fuel_multiplier),"\t",x[0].get_type().get_typeName())
        for x in self.fuel.get_cpu():
            print(math.trunc(x[0].get_quantity()*fuel_multiplier),"\t",x[0].get_type().get_typeName())
        print("Volume per hour: ",total_volume," m^3")
        print("Volume total: ",total_volume*math.trunc(fuel_multiplier)," m^3")
        print("Hours of operation: ",math.trunc(fuel_multiplier))
        time = datetime.timedelta(hours=math.trunc(fuel_multiplier))
        print("Operating time: ",str(time))
        
    def max_stront(self):
        reinforce_volume=0
        for x in self.fuel.get_reinforce():
            reinforce_volume+=x[0].get_volume()
        
if __name__ == '__main__':
    test = POS(27597,1,1,500001)
    test.max_fuel()
    pass