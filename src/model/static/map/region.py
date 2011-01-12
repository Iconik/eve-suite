'''
Created on Oct 28, 2009

@author: frederikns
'''
from model.flyweight import Flyweight

class Region(Flyweight):
    def __init__(self, region_id):
        #prevents reinitializing
        if "inited" in self.__dict__:
            return
        self.inited = None
        #prevents reinitializing