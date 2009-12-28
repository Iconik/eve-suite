'''
Created on Nov 26, 2009

@author: frederikns
'''
from weakref import WeakValueDictionary

poses = WeakValueDictionary()
pos_fuels = WeakValueDictionary()
    
def get_pos_fuel(id):
    from model.static.pos.pos_fuel import POSFuel
    if id not in pos_fuels:
        pos_fuel = POSFuel(id)
        pos_fuels[id] = pos_fuel 
    return pos_fuels[id]