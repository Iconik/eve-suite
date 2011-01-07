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


class BlueprintCalculatorView():
    """Control class for the Blueprint Calculator View"""
    
    def __init__(self, parent):
        self.frame = None
        self.blueprint_combo = None
        self.character_combo = None
        self.material_tree = None
        self.blueprint_tree = None
        
        self.blueprint_calculator = BlueprintCalculator()
        self.last_run = 0
        
        self.res = xrc.XmlResource(
            "view/blueprintcalculator/blueprint_calculator.xrc")
        self.init_frame()
        
    def init_frame(self):
        """initializes the frame"""
        
        self.frame = self.res.LoadFrame(None, "blueprint_calc_frame")
        self.blueprint_combo = xrc.XRCCTRL(self.frame, "blueprint_combo")
        self.character_combo = xrc.XRCCTRL(self.frame, "character_choice")
        self.material_tree = xrc.XRCCTRL(self.frame, "material_tree")
        self.blueprint_tree = xrc.XRCCTRL(self.frame, "blueprint_tree")
        
        self.frame.Bind(wx.EVT_TEXT, self.update_blueprint_list,
            self.blueprint_combo)
        self.frame.Bind(wx.EVT_COMBOBOX, self.update_blueprint,
            self.blueprint_combo)
        self.frame.Bind(wx.EVT_TEXT_ENTER, self.update_blueprint,
            self.blueprint_combo)
        
        self.blueprint_combo.SetItems(self.blueprint_calculator.blueprint_list)
        
        self.frame.Fit()
        self.frame.Show()
        
    def update_blueprint_list(self, event):
        """This function runs each time the blueprint selection combo is
        modified, updating the list of blueprints to only show the ones which
        match the entered substring"""
        
        self.blueprint_combo.SetItems([blueprint for blueprint in 
            self.blueprint_calculator.blueprint_list
            if self.blueprint_combo.Value in blueprint])
        
    def update_blueprint(self, event):
        """This function runs when a blueprint has been selected, displaying
        the resources required for production""" 
        
        if(self.blueprint_combo.Value in
            self.blueprint_calculator.blueprint_list or 
            self.blueprint_combo.Value+" Blueprint" in
            self.blueprint_calculator.blueprint_list):
            print(self.blueprint_calculator.blueprint_map[
                self.blueprint_combo.Value])
            
            self.blueprint_calculator.blueprint_change(
                self.blueprint_calculator.blueprint_map[
                    self.blueprint_combo.Value])