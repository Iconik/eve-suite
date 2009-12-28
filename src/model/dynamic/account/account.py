'''
Created on Nov 6, 2009

@author: frederikns
'''
from model.dynamic.api import api
from model.dynamic.character.character import Character
import xml.etree.ElementTree as ET

class Account(object):
    '''
    classdocs
    '''

    def __init__(self,userID,apiKey):
        '''
        Constructor
        '''
        self.userID = int(userID)
        self.apiKey = apiKey.strip()
        
        api.fetch("account","Characters",self.userID,self.apiKey)
        
        tree = ET.parse("%s/Characters.xml.aspx" % (api.build_path("account",self.userID)))
        root = tree.getroot()
        rowset = root.find("result").find("rowset")
        
        self.characters = list()
        
        for element in rowset:
            self.characters.append(Character(self,element.get("name"),int(element.get("characterID")),element.get("corporationName"),int(element.get("corporationID"))))
        
    def get_userID(self):
        return self.userID
    
    def get_apiKey(self):
        return self.apiKey
    
    def get_characters(self):
        return self.characters
    
    def fetch_skill_queues(self):
        for char in self.characters:
            char.fetch_skill_queue()