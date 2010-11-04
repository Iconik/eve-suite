import wx
from wx import combo

class AutoComboPopup(wx.ListBox, combo.ComboPopup):
    def __init__(self):
        
        self.PostCreate(wx.PreListBox())
        
        # Also init the ComboPopup base class.
        combo.ComboPopup.__init__(self)
        #self.combo = None
        
        items = list()
        inactive_items = list()
        active_items = list()
        
    def AddItem(self, txt):
        self.InsertStringItem(self.GetCount(), txt)

    def OnMotion(self, evt):
        item = self.HitTest(evt.GetPosition())
        if item >= 0:
            self.SetSelection(item)
            self.curitem = item

    def OnLeftDown(self, evt):
        self.value = self.curitem
        #self.Dismiss()
        
    def Selection(self, evt):
        self.curitem = self.GetSelection()
        self.GetCombo().SetValue("test")
        self.Dismiss()
        
    def ApplyFilter(self, string):
        for item in range(0,):
            if string not in item:
                self.inactive_items.append(item)
                self.Delete()

    # The following methods are those that are overridable from the
    # ComboPopup base class.  Most of them are not required, but all
    # are shown here for demonstration purposes.

    # This is called immediately after construction finishes.  You can
    # use self.GetCombo if needed to get to the ComboCtrl instance.
    def Init(self):
        self.value = -1
        self.curitem = -1
        
    def Create(self, parent):
        wx.ListBox.Create(self, parent, style=wx.LB_SINGLE|wx.LB_SORT)
        #self.Bind(wx.EVT_MOTION, self.OnMotion)
        #self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LISTBOX, self.Selection)

    # Return the widget that is to be used for the popup
    def GetControl(self):
        return self

    # Called just prior to displaying the popup, you can use it to
    # 'select' the current item.
    def SetStringValue(self, val):
        idx = self.FindString(val)
        if idx != wx.NOT_FOUND:
            self.SetSelection(idx)

    # Return a string representation of the current item.
    def GetStringValue(self):
        if self.value >= 0:
            return self.GetItemText(self.value)
        return ""

    # Called immediately after the popup is shown
    def OnPopup(self):
        combo.ComboPopup.OnPopup(self)

    # Called when popup is dismissed
    def OnDismiss(self):
        combo.ComboPopup.OnDismiss(self)

    # This is called to custom paint in the combo control itself
    # (ie. not the popup).  Default implementation draws value as
    # string.
    def PaintComboControl(self, dc, rect):
        combo.ComboPopup.PaintComboControl(self, dc, rect)

    # Receives key events from the parent ComboCtrl.  Events not
    # handled should be skipped, as usual.
    def OnComboKeyEvent(self, event):
        combo.ComboPopup.OnComboKeyEvent(self, event)

    # Implement if you need to support special action when user
    # double-clicks on the parent wxComboCtrl.
    def OnComboDoubleClick(self):
        combo.ComboPopup.OnComboDoubleClick(self)

    # Return final size of popup. Called on every popup, just prior to OnPopup.
    # minWidth = preferred minimum width for window
    # prefHeight = preferred height. Only applies if > 0,
    # maxHeight = max height for window, as limited by screen size
    #   and should only be rounded down, if necessary.
    def GetAdjustedSize(self, minWidth, prefHeight, maxHeight):
        return combo.ComboPopup.GetAdjustedSize(self, minWidth, prefHeight, maxHeight)

    # Return true if you want delay the call to Create until the popup
    # is shown for the first time. It is more efficient, but note that
    # it is often more convenient to have the control created
    # immediately.    
    # Default returns false.
    def LazyCreate(self):
        return combo.ComboPopup.LazyCreate(self)
        
        
"""
self.listview_combo = \
    wx.combo.ComboCtrl(self,style=wx.CB_DROPDOWN|wx.CB_READONLY|wx.CB_SORT)
self.listview_popup_ctrl = ListViewComboPopup()
self.listview_combo.SetPopupControl(self.listview_popup_ctrl)
"""