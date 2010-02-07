'''
Created on Nov 26, 2009

@author: frederikns
'''
from weakref import WeakValueDictionary

POSES = WeakValueDictionary()
POS_FUELS = WeakValueDictionary()
    
def get_pos_fuel(pos_type_id):
    """Retrieves or populates the requested pos fuels"""
    from model.static.pos.pos_fuel import POSFuel
    if pos_type_id not in POS_FUELS:
        pos_fuel = POSFuel(pos_type_id)
        POS_FUELS[pos_type_id] = pos_fuel 
    return POS_FUELS[pos_type_id]