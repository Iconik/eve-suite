'''
Created on Nov 2, 2009

@author: frederikns
'''

import urllib
import os
from datetime import datetime
from xml.etree.ElementTree import ElementTree

def build_link(folder,file,userID=None,apiKey=None,characterID=None):
    if userID is not None:
        if apiKey is not None:
            if characterID is not None:
                return "http://api.eve-online.com/%s/%s.xml.aspx?userID=%s&apiKey=%s&characterID=%s" % (folder,file,userID,apiKey,characterID)
            return "http://api.eve-online.com/%s/%s.xml.aspx?userID=%s&apiKey=%s" % (folder,file,userID,apiKey)
        return "http://api.eve-online.com/%s/%s.xml.aspx?userID=%s" % (folder,file,userID)
    return "http://api.eve-online.com/%s/%s.xml.aspx" % (folder,file)
    
def build_path(folder,userID=None,characterID=None,file=None):
    if file is not None:
        if userID is not None:
            if characterID is not None:
                return "../Resources/API Cache/User %s/Character %s/%s/%s.xml.aspx" % (userID,characterID,folder,file)
            return "../Resources/API Cache/User %s/%s/%s.xml.aspx" % (userID,folder,file)
        return "../Resources/API Cache/User %s/%s.xml.aspx" % (userID,file)
    if userID is not None:
        if characterID is not None:
            return "../Resources/API Cache/User %s/Character %s/%s" % (userID,characterID,folder)
        return "../Resources/API Cache/User %s/%s" % (userID,folder)
    return "../Resources/API Cache/User %s" % (userID)

def check_cached_until(path):
    if(os.access(path,os.F_OK)):
        root = ElementTree(file=path)
        cached = root.find("cachedUntil")
        if cached!=None and datetime.utcnow()>datetime.strptime(cached.text,"%Y-%m-%d %H:%M:%S"):
            return True
    return True
    
_online_ = True
    
def fetch(folder,file,userID=None,apiKey=None,characterID=None):
    if not _online_:
        return
    xmlconnection = urllib.urlopen(build_link(folder, file, userID, apiKey, characterID))
    path = build_path(folder, userID, characterID)
    if not os.path.exists(path):
        os.makedirs(path)
    path = build_path(folder, userID, characterID, file)
    if check_cached_until(path):
        output = open(path,'wb')
        output.write(xmlconnection.read())
        output.close()