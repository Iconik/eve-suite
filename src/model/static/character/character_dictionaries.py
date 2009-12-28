'''
Created on 23 Dec 2009

@author: FrederikNS
'''
from weakref import WeakValueDictionary

factions = WeakValueDictionary()
races = WeakValueDictionary()

def get_faction(faction_id):
    from model.static.character.faction import Faction
    if faction_id not in factions:
        faction = Faction(faction_id)
        factions[faction_id] = faction
    return factions[faction_id]

def get_race(race_id):
    from model.static.character.race import Race
    if race_id not in races:
        race = Race(race_id)
        races[race_id] = race
    return factions[race_id]