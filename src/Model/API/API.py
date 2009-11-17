'''
Created on Nov 2, 2009

@author: frederikns
'''

import urllib.request
import os
from datetime import datetime
from xml.etree.ElementTree import ElementTree

def build_link(folder,file,userID,apiKey,characterID):
    url = "http://api.eve-online.com/"+folder+"/"+file+".xml.aspx"
    if userID!=None:
        url+="?userID="+str(userID)
        if apiKey!=None:
            url+="&apiKey="+apiKey
            if characterID!=None:
                url+="&characterID="+str(characterID)
        return url
    
def build_path(folder,userID,characterID=None):
    path = "../../../Resources/API Cache"
    if userID!=None:
        path+="/User "+str(userID)
        if characterID!=None:
            path+="/Character "+str(characterID)
        if folder!=None:
            path+="/"+folder
    return path

def check_cached_until(path):
    if(os.access(path,os.F_OK)):
        root = ElementTree(file=path)
        cached = root.find("cachedUntil")
        if cached!=None and datetime.utcnow()>datetime.strptime(cached.text,"%Y-%m-%d %H:%M:%S"):
            return True
        return False
    return True
    
_online_ = False
    
def fetch(folder,file,userID=None,apiKey=None,characterID=None):
    if not _online_:
        return
    xmlconnection = urllib.request.urlopen(build_link(folder,file,userID,apiKey,characterID))
    path = build_path(folder, userID, characterID)
    if not os.path.exists(path):
        os.makedirs(path)
    if check_cached_until(path+"/"+file+".xml.aspx"):
        output = open(path+"/"+file+".xml.aspx",'wb')
        output.write(xmlconnection.read())
        output.close()