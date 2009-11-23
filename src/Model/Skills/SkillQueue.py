'''
Created on Nov 6, 2009

@author: frederikns
'''
import xml.etree.ElementTree as ElementTree
from Model.API import API
from Model.Skills.SkillQueueItem import SkillQueueItem

class SkillQueue(object):
    '''
    classdocs
    '''

    def __init__(self,userID,apiKey,characterID):
        '''
        Constructor
        '''
        API.fetch("char", "SkillQueue", userID, apiKey, characterID)
        
        tree = ElementTree.parse("%s /SkillQueue.xml.aspx" % API.build_path("char", userID, characterID))
        root = tree.getroot()
        rowset = root.find("result").find("rowset")
        self.skillQueue = list()
        if rowset.getchildren():
            
        
            for element in rowset:
                self.skillQueue.insert(int(element.get("queuePosition")),
                                       SkillQueueItem(int(element.get("typeID")),
                                                      int(element.get("level")),
                                                      int(element.get("startSP")),
                                                      int(element.get("endSP")),
                                                      element.get("startTime"),
                                                      element.get("endTime")))
        
    def get_skill_queue(self):
        return self.skillQueue