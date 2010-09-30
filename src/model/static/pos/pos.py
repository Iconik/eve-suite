'''
Created on Nov 15, 2009

@author: frederikns
'''
from model.static.inv import inventory_dictionaries
from model.static.pos import pos_dictionaries
from model.static.chr import character_dictionaries

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
        self.faction = None
        
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
        
        for online in self.get_fuel().online:
            if online[2] == self.faction or online[2] is None:
                online_volume += online[0].get_volume()
        
        for power in self.fuel.power:
            power_volume += power[0].get_volume()
        power_volume = power_volume * self.power
        
        for cpu in self.fuel.cpu:
            cpu_volume += cpu[0].get_volume()
        cpu_volume = cpu_volume * self.cpu
        
        total_volume = online_volume + power_volume + cpu_volume
        
        fuel_multiplier = math.trunc(self.get_type().capacity / total_volume)
        
        print "Tower: ", self.get_type().type_name
        
        print "Online:"
        for online in self.get_fuel().online:
            if online[2] == self.faction or online[2] == None:
                print online[0].quantity * fuel_multiplier,\
                      "\t", online[0].get_type().type_name
        print "Power:"
        for power in self.get_fuel().power:
            print math.trunc(math.ceil(power[0].quantity * self.power)) * fuel_multiplier, "\t",\
                  power[0].get_type().type_name
        print "CPU:"
        for cpu in self.get_fuel().cpu:
            print math.trunc(math.ceil(cpu[0].quantity * self.cpu)) * fuel_multiplier, "\t",\
                  cpu[0].get_type().type_name
                  
        print "Volume per hour: ", total_volume, " m^3"
        print "Volume total: ", total_volume * fuel_multiplier,\
              " m^3"
        print "Hours of operation: ", fuel_multiplier
        time = datetime.timedelta(hours=fuel_multiplier)
        print "Operating time: ", str(time)
        
    def max_stront(self):
        """Calculates and prints the optimal strontium amount for the pos"""
        reinforce_volume = 0
        for reinforce in self.fuel.get_reinforce():
            reinforce_volume += reinforce[0].get_volume()
        print reinforce_volume
        
if __name__ == '__main__':
    TEST = POS(27597, 840000.0/1275000.0, 3500.0/3750.0, 500001)
    TEST.max_fuel()
