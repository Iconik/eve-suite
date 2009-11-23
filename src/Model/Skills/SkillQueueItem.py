'''
Created on Nov 6, 2009

@author: frederikns
'''
from Model.RomanNumeral import RomanNumeral
from Model.Type.Type import Type
from datetime import datetime

class SkillQueueItem(object):
    '''
    classdocs
    '''

    def __init__(self,typeID,level,startSP,endSP,startTime,endTime):
        '''
        Constructor
        '''
        self.type = Type(typeID)
        self.level = RomanNumeral.int_to_roman(level)
        self.startSP = startSP
        self.endSP = endSP
        if len(startTime)>0:
            self.startTime = datetime.strptime(startTime,"%Y-%m-%d %H:%M:%S")
        else:
            self.startTime = None
        if len(endTime)>0:
            self.endTime = datetime.strptime(endTime,"%Y-%m-%d %H:%M:%S")
        else:
            self.endTime = None
        
    def get_type(self):
        return self.type
    
    def get_name(self):
        return self.type.get_typeName()
    
    def get_level(self):
        return self.level
    
    def get_startSP(self):
        return self.startSP
    
    def get_endSP(self):
        return self.endSP
    
    def get_startTime(self):
        return self.startTime
    
    def get_endTime(self):
        return self.endTime