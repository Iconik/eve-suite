'''
Created on Nov 6, 2009

@author: frederikns
'''

from model.dynamic.skills.skill_queue import SkillQueue


class Character(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_hdmBUhEPEd-LgJ4IxcJkTA
    """

    def __init__(self, account, name, character_id, #IGNORE:R0913
                 corporation_name, corporation_id):
        '''
        Constructor
        '''
        self.account = account
        self.name = name
        self.character_id = character_id
        self.corporation_name = corporation_name
        self.corporation_id = corporation_id
        
        self.skill_queue = None
    
    def get_skill_queue(self):
        """Populates and returns the characters skill queue"""
        if self.skill_queue is None:
            self.skill_queue = SkillQueue(self.account.get_userID(),
                                         self.account.get_apiKey(),
                                         self.character_id)
        return self.skill_queue.get_skill_queue()
        
