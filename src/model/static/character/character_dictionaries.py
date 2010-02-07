'''
Created on 23 Dec 2009

@author: FrederikNS
'''
from weakref import WeakValueDictionary

FACTIONS = WeakValueDictionary()
RACES = WeakValueDictionary()

def get_faction(faction_id):
    """Loads and returns the faction specified"""
    from model.static.character.faction import Faction
    if faction_id not in FACTIONS:
        faction = Faction(faction_id)
        FACTIONS[faction_id] = faction
    return FACTIONS[faction_id]

def get_race(race_id):
    """Loads and returns the race specified"""
    from model.static.character.race import Race
    if race_id not in RACES:
        race = Race(race_id)
        RACES[race_id] = race
    return RACES[race_id]