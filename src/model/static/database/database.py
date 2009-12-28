'''
Created on Dec 7, 2009

@author: frederikns
'''
import sqlite3

location = '../Resources/Database/dom100-sqlite3-v1.db'

connection = sqlite3.connect(location)
connection.row_factory = sqlite3.Row

def get_cursor(statement=None):
    cursor = connection.cursor()
    if statement is not None:
        cursor.execute(statement)
    return cursor

""" SQL to Class variables
replace .*"(.*)".*
with         self.\1 = row["\1"]
"""