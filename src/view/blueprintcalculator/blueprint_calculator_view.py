'''
Created on Oct 28, 2009

@author: frederikns
'''
import wx
from wx import xrc
from wx import combo
from wx import gizmos
from modelview.blueprintcalculator.blueprint_calculator import BlueprintCalculator

class BlueprintCalculatorView:
    def __init__(self):
        self.res = xrc.XmlResource('view/blueprintcalculator/blueprint_calculator.xrc')
        self.init_frame()
        self.blueprint_calculator = BlueprintCalculator()
        #self.blueprint_combo.AppendItems(self.blueprint_calculator.blueprint_list)
        
    def init_frame(self):
        self.frame = self.res.LoadFrame(None, 'blueprint_calc_frame')
        
        self.blueprint_combo = combo.ComboCtrl(self.frame)
        self.res.AttachUnknownControl("blueprint_combo", self.blueprint_combo,
                                      self.frame)
        
        
        self.material_tree = gizmos.TreeListCtrl(self.frame)
        self.res.AttachUnknownControl('material_tree', self.material_tree,
                                      self.frame)
        
        self.frame.Show()

'''
from PyQt4 import QtGui, QtCore

from view.blueprintcalculator.blueprint_calculator_template import \
Ui_MainWindow

from model.static.database import database
from model.generated.number.number import format_number
from model.dynamic.inventory.blueprint import Blueprint
from modelview.blueprintcalculator.blueprint_calculator import BlueprintCalculator

class BlueprintCalculatorView(QtGui.QMainWindow):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EITQYxEREd-LgJ4IxcJkTA
    """
    def __init__(self, parent=None): #IGNORE:W0231
        QtGui.QWidget.__init__(self, parent) #IGNORE:W0233
        self.ui = Ui_MainWindow() #IGNORE:C0103
        self.ui.setupUi(self)
        self.ui.material_table.setAlternatingRowColors(True)
        self.ui.material_table.setUniformRowHeights(True)
        for col in range(0,self.ui.material_table.columnCount()):
            self.ui.material_table.resizeColumnToContents(col)

        backend = BlueprintCalculator()
        
        self.material_categories = dict()
        
        skill_levels = ["N", "I", "II", "III", "IV", "V"]
        self.ui.pe_skill_combo.addItems(skill_levels)
        
        
        
        self.connect(self.ui.me_spin, QtCore.SIGNAL('valueChanged(int)'),
                     self.populate_materials)
        self.connect(self.ui.runs_spin, QtCore.SIGNAL('valueChanged(int)'),
                     self.populate_materials)
        self.connect(self.ui.blueprint_combo,
                     QtCore.SIGNAL('currentIndexChanged(int)'),
                     self.populate_materials)
        self.connect(self.ui.pe_skill_combo,
                     QtCore.SIGNAL('currentIndexChanged(int)'),
                     self.populate_materials)
        
    def populate_blueprints(self):
        """
        Fetches a list of blueprints, and populates the blueprint selector with
        them
        """
        cursor = database.get_cursor("SELECT typeID, typeName FROM \
        invBlueprintTypes LEFT JOIN invTypes ON blueprintTypeID=typeID WHERE \
        published=1 ORDER BY typeName")
        self.blueprint_map = dict()
        self.blueprints = list()
        for row in cursor:
            self.blueprint_map[row["typeName"]] = row["typeID"]
            self.blueprints.append(row["typeName"])
        self.ui.blueprint_combo.addItems(self.blueprints)
        self.ui.blueprint_combo.setEditText("")
        QtGui.QCompleter(self.blueprints, self.ui.blueprint_combo)
        self.ui.blueprint_combo.completer().setCompletionMode(
            QtGui.QCompleter.PopupCompletion)
        cursor.close()
        
    def populate_skill_combo(self):
        """
        Populates the skill selection combos with the available skill levels
        """
        
    def populate_materials(self):
        """Populates the material tree view"""
        if str(self.ui.blueprint_combo.currentText()) != str():
            self.blueprint = Blueprint(
                self.blueprint_map[str(self.ui.blueprint_combo.currentText())])
        self.blueprint.material_efficiency = int(self.ui.me_spin.text())
        materials = self.blueprint.get_combined(
            self.ui.pe_skill_combo.currentIndex())
        requirements = self.blueprint.get_requirements().requirements
        
        self.ui.material_table.clear()
        self.material_categories.clear()
        
        for mat in materials:
            if (mat[0].get_type().get_group().category_id not in
                self.material_categories):
                self.material_categories[
                    mat[0].get_type().get_group().category_id] = (
                        QtGui.QTreeWidgetItem(
                            self.ui.material_table,
                            [mat[0].get_type().get_group().get_category().category_name]))
                self.material_categories[
                    mat[0].get_type().get_group().category_id].setExpanded(True)
            
            QtGui.QTreeWidgetItem(
                self.material_categories[
                    mat[0].get_type().get_group().category_id],
                QtCore.QStringList(
                    [mat[0].get_type().type_name,
                     format_number(mat[0].quantity *
                                   int(self.ui.runs_spin.text())),
                     format_number(mat[1] * int(self.ui.runs_spin.text())),
                     format_number(mat[2] * int(self.ui.runs_spin.text())),
                     "",
                     "",
                     format_number(mat[3]),
                     format_number(mat[4])]))
        
        for req in requirements[1]:
            if (req[0].get_type().get_group().category_id not in
                self.material_categories):
                self.material_categories[
                    req[0].get_type().get_group().category_id] = (
                        QtGui.QTreeWidgetItem(
                            self.ui.material_table,
                            [req[0].get_type().get_group().get_category().category_name]))
                self.material_categories[
                    req[0].get_type().get_group().category_id
                    ].setExpanded(True)
            
            QtGui.QTreeWidgetItem(
                self.material_categories[
                    req[0].get_type().get_group().category_id],
                QtCore.QStringList(
                    [req[0].get_type().type_name, 
                     format_number(
                        (req[0].quantity * int(self.ui.runs_spin.text())) if 
                        req[0].get_type().get_group().category_id != 16 else
                        req[0].quantity),
                        "",
                     format_number(
                        (req[0].quantity * int(self.ui.runs_spin.text())) if 
                        req[0].get_type().get_group().category_id != 16 else
                        req[0].quantity)]))
        
        for col in range(0, self.ui.material_table.columnCount()):
            self.ui.material_table.resizeColumnToContents(col)
'''