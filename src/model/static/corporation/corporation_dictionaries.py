'''
Created on 23 Dec 2009

@author: FrederikNS
'''
from weakref import WeakValueDictionary

npc_corporations = WeakValueDictionary()

def get_corporation(corporation_id):
    return get_npc_corporation(corporation_id)
    
def get_npc_corporation(corporation_id):
    from model.static.corporation.npc_corporation import NPCCorporation
    if corporation_id not in npc_corporations:
        npc_corporation = NPCCorporation(corporation_id)
        npc_corporations[corporation_id] = npc_corporation
    return npc_corporations[corporation_id]