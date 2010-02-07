'''
Created on 23 Dec 2009

@author: FrederikNS
'''
from weakref import WeakValueDictionary

NPC_CORPORATIONS = WeakValueDictionary()
    
def get_npc_corporation(corporation_id):
    """Retrieves or populates the requested NPC Corporation"""
    from model.static.corporation.npc_corporation import NPCCorporation
    if corporation_id not in NPC_CORPORATIONS:
        npc_corporation = NPCCorporation(corporation_id)
        NPC_CORPORATIONS[corporation_id] = npc_corporation
    return NPC_CORPORATIONS[corporation_id]