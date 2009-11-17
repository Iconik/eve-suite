'''
Created on Oct 28, 2009

@author: frederikns
'''

import sqlite3

class SolarSystem(object):
    '''
    classdocs
    '''

    def __init__(self,id):
        '''
        Constructor
        '''
        self.solarSystemID = id
        conn = sqlite3.connect('../../../Resources/Database/apo15-sqlite3-v1.db')
        cur = conn.cursor()
        cur.execute("select * from mapSolarSystem where solarSystemID='"+str(self.solarSystemID)+"';")
        row = cur.fetchone()
        
        self.regionID = row[0]
        self.constellationID = row[1]
        self.solarSystemName = row[3]
        self.x = row[4]
        self.y = row[5]
        self.z = row[6]
        self.xMin = row[7]
        self.xMax = row[8]
        self.yMin = row[9]
        self.yMax = row[10]
        self.zMin = row[11]
        self.zMax = row[12]
        self.luminosity = row[13]
        self.border = row[14]
        self.fringe = row[15]
        self.corridor = row[16]
        self.hub = row[17]
        self.international = row[18]
        self.regional = row[19]
        self.constellation = row[20]
        self.security = row[21]
        self.factionID = row[22]
        self.radius = row[23]
        self.sunTypeID = row[24]
        self.securityClass = row[25]
        
        cur.close()
        conn.close()