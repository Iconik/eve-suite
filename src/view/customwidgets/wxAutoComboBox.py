import wx
from wx import combo
from view.customwidgets.wxAutoComboPopup import AutoComboPopup

class AutoComboBox(combo.ComboCtrl):
    def __init__(self, parent, style=0):
        combo.ComboCtrl.__init__(self, parent, style=style)
        self.popup = AutoComboPopup()
        self.popup.combo = self
        self.SetPopupControl(self.popup)
        
        self.Bind(wx.EVT_TEXT, self.update_popup)
        self.items = list()
        
    def AppendItems(self, list):
        self.popup.AppendItems(list)
        
    def update_popup(self, event):
        self.GetPopupControl().ApplyFilter(self.GetValue())
        #do stuff
        
        """if not self.IsPopupShown():
            self.ShowPopup()
        
        self.SetFocus()"""
        
        pass