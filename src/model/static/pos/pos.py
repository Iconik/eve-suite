'''
Created on Nov 15, 2009

@author: frederikns
'''
from model.static.inventory import inventory_dictionaries
from model.static.pos import pos_dictionaries
from model.static.character import character_dictionaries

import datetime
import math

class POS(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EINw0xEREd-LgJ4IxcJkTA
    """

    def __init__(self, type_id, power, cpu, faction_id):
        '''
        Constructor
        '''
        self.type_id = type_id
        self.power = power
        self.cpu = cpu
        self.faction_id = faction_id
        
        self.type = None
        self.fuel = None
        self.faction = faction
        
    def get_type(self):
        """Populates and returns the type"""
        if self.type is None:
            self.type = inventory_dictionaries.get_type(self.type_id)
        return self.type
    
    def get_fuel(self):
        """Populates and returns the fuels"""
        if self.fuel is None:
            self.fuel = pos_dictionaries.get_pos_fuel(self.type_id)
        return self.fuel
    
    def get_faction(self):
        """Populates and returns the faction"""
        if self.faction is None:
            self.faction = character_dictionaries.get_faction(self.faction_id)
        return self.faction
    
    def max_fuel(self):
        """Calculates and prints the optimal fuel composition for the pos"""
        online_volume = 0.0
        power_volume = 0.0
        cpu_volume = 0.0
        
        for online in self.fuel.get_online():
            if online[2] == self.faction or online[2] == None:
                online_volume += online[0].get_volume()
        
        for power in self.fuel.get_power():
            power_volume += power[0].get_volume()
        power_volume *= self.power
        
        for cpu in self.fuel.get_cpu():
            cpu_volume += cpu[0].get_volume()
        cpu_volume *= self.cpu
        
        total_volume = online_volume + power_volume + cpu_volume
        
        fuel_multiplier = self.type.get_capacity() / total_volume
        
        print("Tower: ", self.type.get_typeName())
        
        for online in self.fuel.get_online():
            if online[2] == self.faction or online[2] == None:
                print(math.trunc(online[0].get_quantity() * fuel_multiplier),
                      "\t", online[0].get_type().get_typeName())
        for power in self.fuel.get_power():
            print(math.trunc(power[0].get_quantity() * fuel_multiplier), "\t",
                  online[0].get_type().get_typeName())
        for cpu in self.fuel.get_cpu():
            print(math.trunc(cpu[0].get_quantity() * fuel_multiplier), "\t",
                  cpu[0].get_type().get_typeName())
        print("Volume per hour: ", total_volume, " m^3")
        print("Volume total: ", total_volume * math.trunc(fuel_multiplier),
              " m^3")
        print("Hours of operation: ", math.trunc(fuel_multiplier))
        time = datetime.timedelta(hours=math.trunc(fuel_multiplier))
        print("Operating time: ", str(time))
        
    def max_stront(self):
        """Calculates and prints the optimal strontium amount for the pos"""
        reinforce_volume = 0
        for reinforce in self.fuel.get_reinforce():
            reinforce_volume += reinforce[0].get_volume()
        print reinforce_volume
        
if __name__ == '__main__':
    TEST = POS(27597, 1, 1, 500001)
    TEST.max_fuel()
