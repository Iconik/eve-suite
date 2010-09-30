'''
Created on Nov 2, 2009

@author: frederikns
'''

import urllib
import os
from datetime import datetime
from xml.etree.ElementTree import ElementTree

def build_link(folder, file_name, user_id=None, api_key=None, 
               character_id=None):
    """Builds a link url for an api XML file"""
    if user_id is not None:
        if api_key is not None:
            if character_id is not None:
                return "http://api.eve-online.com/%s/\
                %s.xml.aspx?userID=%s&apiKey=%s&characterID=%s" % \
                (folder, file_name, user_id, api_key, character_id)
            return "http://api.eve-online.com/%s/\
            %s.xml.aspx?userID=%s&apiKey=%s" % \
            (folder, file_name, user_id, api_key)
        return "http://api.eve-online.com/%s/%s.xml.aspx?userID=%s" % \
        (folder, file_name, user_id)
    return "http://api.eve-online.com/%s/%s.xml.aspx" % (folder, file_name)
    
def build_path(folder, user_id=None, character_id=None, file_name=None):
    """Builds a relative file path for an api XML cache file"""
    if file_name is not None:
        if user_id is not None:
            if character_id is not None:
                return "../Resources/API Cache/User %s/Character %s/%s/\
                %s.xml.aspx" % (user_id, character_id, folder, file_name)
            return "../Resources/API Cache/User %s/%s/%s.xml.aspx" % \
            (user_id, folder, file_name)
        return "../Resources/API Cache/User %s/%s.xml.aspx" % \
        (user_id, file_name)
    if user_id is not None:
        if character_id is not None:
            return "../Resources/API Cache/User %s/Character %s/%s" % \
            (user_id, character_id, folder)
        return "../Resources/API Cache/User %s/%s" % (user_id, folder)
    return "../Resources/API Cache/User %s" % (user_id)

def check_cached_until(path):
    """Checks if the cachetime of a XML cache file is still valid"""
    if(os.access(path, os.F_OK)):
        root = ElementTree(file=path)
        cached = root.find("cachedUntil")
        if cached != None and (datetime.utcnow() >
                               datetime.strptime(cached.text,
                                                 "%Y-%m-%d %H:%M:%S")):
            return True
    return True
    
ONLINE = True
    
def fetch(folder, file_name, user_id=None, api_key=None, character_id=None):
    """
    Checks if the specified api XML file is outdated, and if it is, fetches a
    new one online
    """
    if not ONLINE:
        return
    xmlconnection = urllib.urlopen(build_link(folder, file_name, user_id,
                                              api_key, character_id))
    path = build_path(folder, user_id, character_id)
    if not os.path.exists(path):
        os.makedirs(path)
    path = build_path(folder, user_id, character_id, file)
    if check_cached_until(path):
        output = open(path,'wb')
        output.write(xmlconnection.read())
        output.close()