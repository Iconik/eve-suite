'''
Created on Feb 8, 2010

@author: frederikns
'''
import locale

def format_number(number):
    if locale.setlocale(locale.LC_ALL, '') == 'C':
        locale.setlocale(locale.LC_ALL, 'en_GB')
    return locale.format("%d", number, True)