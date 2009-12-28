'''
Created on Nov 26, 2009

@author: frederikns
'''
from weakref import WeakValueDictionary

blueprints = WeakValueDictionary()
types = WeakValueDictionary()
groups = WeakValueDictionary()
categories = WeakValueDictionary()
market_groups = WeakValueDictionary()    

def get_blueprint(blueprint_type_id):
    from model.static.inventory.blueprint_type import BlueprintType
    if blueprint_type_id not in blueprints:
        blueprint = BlueprintType(blueprint_type_id)
        blueprints[blueprint_type_id] = blueprint
    return blueprints[blueprint_type_id] 

def get_type(type_id):
    from model.static.inventory.type import Type
    if type_id not in types:
        type = Type(type_id)
        types[type_id] = type
    return types[type_id]
    
def get_group(group_id):
    from model.static.inventory.group import Group
    if group_id not in groups:
        group = Group(group_id)
        groups[group_id] = group
    return groups[group_id]
    
def get_category(category_id):
    from model.static.inventory.category import Category
    if category_id not in categories:
        category = Category(category_id)
        categories[category_id] = category
    return categories[category_id]
    
def get_market_group(market_group_id):
    from model.static.inventory.market_group import MarketGroup
    if market_group_id not in market_groups:
        market_group = MarketGroup(market_group_id)
        market_groups[market_group_id] = market_group
    return market_groups[market_group_id]

