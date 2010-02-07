'''
Created on 30 Jan 2010

@author: FrederikNS
'''
from weakref import WeakValueDictionary

ATTRIBUTES = WeakValueDictionary()

def get_attribute(attribute_id):
    """Retrieves or populates the requested NPC Corporation"""
    from model.static.dgm.attribute import Attribute
    if attribute_id not in ATTRIBUTES:
        attribute = Attribute(attribute_id)
        ATTRIBUTES[attribute_id] = attribute 
    return ATTRIBUTES[attribute_id]