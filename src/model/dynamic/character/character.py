'''
Created on Nov 6, 2009

@author: frederikns
'''
from model.dynamic.skills.skill_queue import SkillQueue


class Character(object):
    '''
    classdocs
    '''


    def __init__(self,account,name,characterID,corporationName,corporationID):
        '''
        Constructor
        '''
        self.account = account
        self.name = name
        self.characterID = characterID
        self.corporationName = corporationName
        self.corporationID = corporationID
    
    def get_account(self):
        return self.account
    
    def get_name(self):
        return self.name
    
    def get_characterID(self):
        return self.character    
    
    def get_corporationName(self):
        return self.corporationName
    
    def get_corporationID(self):
        return self.corporationID
    
    def get_skill_queue(self):
        if 'self.skillQueue' not in locals():
            self.skillQueue = SkillQueue(self.account.get_userID(),self.account.get_apiKey(),self.characterID)
        return self.skillQueue.get_skill_queue()
        