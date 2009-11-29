'''
Created on Nov 6, 2009

@author: frederikns
'''
from Model.API import API
from Model.Character.Character import Character
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
        
        API.fetch("account","Characters",self.userID,self.apiKey)
        
        tree = ET.parse("%s/Characters.xml.aspx" % (API.build_path("account",self.userID)))
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
    
if __name__ == '__main__':
    userID=2698778
    apiKey="VD6mibIWqvNLZVtfmBgyAJJUASc5ADV0PylBAeIsgJWUTcAYTOgEUPe59482Gq8M"
    account = Account(userID,apiKey)
    characters = account.characters
    for character in account.characters:
        print(character.get_name()+":")
        for skill in character.get_skill_queue():
            if skill.get_startTime():
                print("\t%s %s\t%s" % (skill.get_name(),skill.get_level(),skill.get_startTime().isoformat(" ")))
            if skill.get_endTime():
                print("\t%s %s\t%s" % (skill.get_name(),skill.get_level(),skill.get_endTime().isoformat(" ")))
        print()