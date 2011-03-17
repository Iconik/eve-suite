'''
Created on Oct 28, 2009

@author: frederikns
'''
from model.flyweight import Flyweight

class Region(Flyweight):
    def __init__(self, region_id):
        #prevents reinitializing
        if "_inited" in self.__dict__:
            return
        self._inited = None
        #prevents reinitializing