'''
Created on 23 Dec 2009

@author: FrederikNS
'''
from model.static.database import database

class Race(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EH5AsBEREd-LgJ4IxcJkTA
    """

    def __init__(self, race_id):
        '''
        Constructor
        '''
        self.race_id = race_id
        
        cursor = database.get_cursor("select * from chrRaces where \
        raceID='%s';" % (self.race_id))
        row = cursor.fetchone()
        
        self.race_name = row["raceName"]
        self.description = row["description"]
        self.graphic_id = row["graphicID"]
        self.short_description = row["shortDescription"]
