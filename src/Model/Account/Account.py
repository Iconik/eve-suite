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
        self.userID = userID
        self.apiKey = apiKey
        
        API.fetch("account","Characters",self.userID,self.apiKey)
        
        tree = ET.parse(API.build_path("account",userID)+"/Characters.xml.aspx")
        root = tree.getroot()
        rowset = root.find("result").find("rowset")
        
        self.characters = list()
        
        for element in rowset:
            self.characters.append(Character(self,element.get("name"),int(element.get("characterID")),element.get("corporationName"),int(element.get("corporationID"))))
        
    def get_userID(self):
        return self.userID
    
    def get_apiKey(self):
        return self.apiKey
    
    def fetch_skill_queues(self):
        for char in self.characters:
            char.fetch_skill_queue()
    
if __name__ == '__main__':
    userID=0
	apiKey=0
    account = Account(userID,apiKey)
    account.fetch_skill_queues()
    for character in account.characters:
        print(character.get_name()+":")
        for skill in character.get_skill_queue():
            str = "\t"+skill.get_name()+" "+skill.get_level()
            if skill.get_startTime():
                str+="\t"+skill.get_startTime().isoformat(" ")
            if skill.get_endTime():
                str+="\t"+skill.get_endTime().isoformat(" ")
            print(str)
        print()