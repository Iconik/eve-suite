'''
Created on Nov 26, 2009

@author: frederikns
'''
from weakref import WeakValueDictionary
from Model.POS.POS import POS
from Model.POS.POSFuel import POSFuel

class POSDictionaries(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.poses = WeakValueDictionary()
        self.posFuels = WeakValueDictionary()
        
    def get_pos(self,posID):
        if posID not in self.poses:
            pos = POS(posID)
            self.poses[posID] = pos
        return self.poses[posID]
    
    def get_posFuel(self,id):
        if id not in self.posFuels:
            posFuel = POSFuel(id)
            self.posFuels[id] = posFuel 
        return self.posFuels[id]