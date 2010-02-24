'''
Created on 15 Feb 2010

@author: FrederikNS
'''

from weakref import WeakValueDictionary

TYPE_REQUIREMENTS = WeakValueDictionary()

def get_type_requirements(type_id):
    """Retrieves or populates the requested market group"""
    from model.static.ram.type_requirements import TypeRequirements
    if type_id not in TYPE_REQUIREMENTS:
        type_requirements = TypeRequirements(type_id)
        TYPE_REQUIREMENTS[type_id] = type_requirements
    return TYPE_REQUIREMENTS[type_id]
