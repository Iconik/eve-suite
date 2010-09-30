'''
Created on Nov 26, 2009

@author: frederikns
'''
from weakref import WeakValueDictionary

BLUEPRINTS = WeakValueDictionary()
TYPES = WeakValueDictionary()
GROUPS = WeakValueDictionary()
CATEGORIES = WeakValueDictionary()
MARKET_GROUPS = WeakValueDictionary()
TYPE_MATERIALS = WeakValueDictionary()

def get_blueprint(blueprint_type_id):
    """Retrieves or populates the requested blueprint"""
    from model.static.inv.blueprint_type import BlueprintType
    if blueprint_type_id not in BLUEPRINTS:
        blueprint = BlueprintType(blueprint_type_id)
        BLUEPRINTS[blueprint_type_id] = blueprint
    return BLUEPRINTS[blueprint_type_id] 

def get_type(type_id):
    """Retrieves or populates the requested type"""
    from model.static.inv.type import Type
    if type_id not in TYPES:
        type = Type(type_id) #IGNORE:W0622
        TYPES[type_id] = type
    return TYPES[type_id]
    
def get_group(group_id):
    """Retrieves or populates the requested group"""
    from model.static.inv.group import Group
    if group_id not in GROUPS:
        group = Group(group_id)
        GROUPS[group_id] = group
    return GROUPS[group_id]
    
def get_category(category_id):
    """Retrieves or populates the requested category"""
    from model.static.inv.category import Category
    if category_id not in CATEGORIES:
        category = Category(category_id)
        CATEGORIES[category_id] = category
    return CATEGORIES[category_id]
    
def get_market_group(market_group_id):
    """Retrieves or populates the requested market group"""
    from model.static.inv.market_group import MarketGroup
    if market_group_id not in MARKET_GROUPS:
        market_group = MarketGroup(market_group_id)
        MARKET_GROUPS[market_group_id] = market_group
    return MARKET_GROUPS[market_group_id]

def get_type_materials(type_id, blueprint_type_id=None):
    """Retrieves or populates the requested market group"""
    from model.static.inv.type_materials import TypeMaterials
    if type_id not in TYPE_MATERIALS:
        type_materials = TypeMaterials(type_id, blueprint_type_id)
        TYPE_MATERIALS[type_id] = type_materials
    return TYPE_MATERIALS[type_id]
