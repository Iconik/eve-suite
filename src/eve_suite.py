'''
Created on Nov 30, 2009

@author: frederikns
'''
import wx
from view.mainwindow.main_window import MainWindow


class EVESuite(wx.App): #IGNORE:R0904
    """The main class for the eve suite"""
    
    def __init__(self):
        wx.App.__init__(self)
        self.mainframe = None
        
    def OnInit(self): #IGNORE:C0103
        """Function needed for wx, to initialize the program"""
        self.SetAppName('EVE Suite')
        self.mainframe = MainWindow()
        self.SetTopWindow(self.mainframe.frame)
        return True

if __name__ == '__main__':

    APP = EVESuite()
    APP.MainLoop()