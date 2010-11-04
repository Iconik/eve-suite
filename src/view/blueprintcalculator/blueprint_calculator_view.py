'''
Created on Oct 28, 2009

@author: frederikns
'''
import wx
from wx import xrc
from wx import combo

from modelview.blueprintcalculator.blueprint_calculator import \
BlueprintCalculator
from modelview.blueprintcalculator import blueprint_calculator
from view.customwidgets.PromptingComboBox import PromptingComboBox


class BlueprintCalculatorView():
    """Control class for the Blueprint Calculator View"""
    def __init__(self, parent):
        self.frame = None
        self.blueprint_combo = None
        self.character_combo = None
        self.material_tree = None
        self.blueprint_tree = None
        
        self.res = xrc.XmlResource('view/blueprintcalculator/blueprint_calculator.xrc')
        self.init_frame()
        
        self.blueprint_calculator = BlueprintCalculator()
        self.last_run = 0
        
        self.active_blueprints = list(self.blueprint_calculator.blueprint_list)
        self.inactive_blueprints = list()
        self.blueprint_combo.SetItems(self.active_blueprints)
        
    def init_frame(self):
        """initializes the frame"""
        self.frame = self.res.LoadFrame(None, 'blueprint_calc_frame')
        #self.panel = xrc.XRCCTRL(self.frame, "main_panel")
        self.blueprint_combo = wx.ComboBox(self.frame)
        self.res.AttachUnknownControl("blueprint_combo", self.blueprint_combo,
            self.frame)
        self.character_combo = xrc.XRCCTRL(self.frame, "character_combo")
        self.material_tree = xrc.XRCCTRL(self.frame, "material_tree")
        self.blueprint_tree = xrc.XRCCTRL(self.frame, "blueprint_tree")
        
        self.frame.Bind(wx.EVT_TEXT, self.update_blueprint_list,
            self.blueprint_combo)
        self.frame.Bind(wx.EVT_COMBOBOX, self.update_production,
            self.blueprint_combo)
        self.frame.Bind(wx.EVT_TEXT_ENTER, self.update_production,
            self.blueprint_combo)
        
        self.frame.Fit()
        self.frame.Show()
        
    def update_blueprint_list(self, event):
        """This function runs each time the blueprint selection combo is
        modified, updating the list of blueprints to only show the ones which
        match the entered substring"""
        if len(self.blueprint_combo.Value) == 0:
            self.active_blueprints.extend(self.inactive_blueprints)
            self.inactive_blueprints = list()
        elif len(self.blueprint_combo.Value) > self.last_run:
            removals = list()
            for index in xrange(0,len(self.active_blueprints)):
                if self.blueprint_combo.Value not in self.active_blueprints[index]:
                    removals.append(index)
            if len(removals)>0:
                for index in reversed(removals):
                    self.inactive_blueprints.append(self.active_blueprints[index])
                    del self.active_blueprints[index]
        else:
            additions = list()
            for index in xrange(0,len(self.inactive_blueprints)):
                if self.blueprint_combo.Value in self.inactive_blueprints[index]:
                    additions.append(index)
            if len(additions)>0:
                for index in reversed(additions):
                    self.active_blueprints.append(self.inactive_blueprints[index])
                    del self.inactive_blueprints[index]
        self.last_run = len(self.blueprint_combo.Value)
        self.active_blueprints.sort()
        self.blueprint_combo.SetItems(self.active_blueprints)
        
    def update_production(self, event):
        """This function runs when a blueprint has been selected, displaying
        the resources required for production""" 
        pass