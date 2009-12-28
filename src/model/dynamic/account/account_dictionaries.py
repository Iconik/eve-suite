'''
Created on Nov 26, 2009

@author: frederikns
'''
from weakref import WeakValueDictionary

from model.dynamic.account.account import Account

class AccountDictionaries(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.accounts = WeakValueDictionary()
        
    def get_account(self,userID):
        if userID not in self.accounts:
            account = Account(userID)
            self.accounts[userID] = account
        return self.accounts[userID]