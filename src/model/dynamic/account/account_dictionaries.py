'''
Created on Nov 26, 2009

@author: frederikns
'''
from weakref import WeakValueDictionary

ACCOUNTS = WeakValueDictionary()
        
def get_account(self, user_id):
    """
    Checks if the requested account has already been loaded, and if not, id 
    loads it, before returning it
    """
    from model.dynamic.account.account import Account
    if user_id not in self.accounts:
        account = Account(user_id)
        self.accounts[user_id] = account
    return self.accounts[user_id]