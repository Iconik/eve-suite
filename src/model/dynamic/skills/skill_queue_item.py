'''
Created on Nov 6, 2009

@author: frederikns
'''
from datetime import datetime
from model.generated.roman.roman import to_roman

class SkillQueueItem(object):
    def __init__(self, type_id, level, start_sp, end_sp, #IGNORE:R0913
                 start_time, end_time):
        self.type_id = type_id
        self.level = to_roman(level)
        self.start_sp = start_sp
        self.end_sp = end_sp
        if len(start_time)>0:
            self.start_time = datetime.strptime(start_time,
                                                "%Y-%m-%d %H:%M:%S")
        else:
            self.start_time = None
        if len(end_time)>0:
            self.end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        else:
            self.end_time = None
        
        self.type = None
            
    def get_type(self):
        """Populates and returns the type"""
        if self.type is None:
            from model.static.inv.type import Type
            self.type = Type(self.type_id)
        return self.type
