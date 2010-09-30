'''
Created on Oct 28, 2009

@author: frederikns
'''
import wx
from wx import xrc
from view.blueprintcalculator.blueprint_calculator_view import BlueprintCalculatorView

class MainWindow: #IGNORE:R0904
    def __init__(self):
        self.res = xrc.XmlResource('view/mainwindow/main_window.xrc')
        self.init_frame()
    
    def init_frame(self):
        self.frame = self.res.LoadFrame(None, 'main_frame')
        self.frame.Bind(wx.EVT_BUTTON, self.blueprint_calc, id=xrc.XRCID('blueprint_calculator_button'))
        self.frame.Show()
        
    def blueprint_calc(self, event):
        bpc = BlueprintCalculatorView()