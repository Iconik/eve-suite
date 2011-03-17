'''
Created on Dec 7, 2009

@author: frederikns
'''
import sqlite3

LOCATION = '../Resources/Database/inc110-sqlite3-v1.db'

CONNECTION = sqlite3.connect(LOCATION)
CONNECTION.row_factory = sqlite3.Row

def get_cursor(statement=None):
    """Instantiates a cursor, runs the requested statement and returns it"""
    cursor = CONNECTION.cursor()
    if statement is not None:
        cursor.execute(statement)
    return cursor

""" SQL to Class variables
replace .*"(.*)".*
with         self.\1 = row["\1"]
""" #IGNORE:W0105