'''
Created on Oct 28, 2009

@author: frederikns
'''
from PyQt4 import QtGui, QtCore

from view.blueprintcalculator.blueprint_calculator_template import \
Ui_MainWindow

from model.static.database import database
from model.generated.roman import roman
from model.static.inventory.inventory_dictionaries import get_blueprint

class BlueprintCalculator(QtGui.QMainWindow):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EITQYxEREd-LgJ4IxcJkTA
    """
    def __init__(self, parent=None): #IGNORE:W0231
        QtGui.QWidget.__init__(self, parent) #IGNORE:W0233
        self.ui = Ui_MainWindow() #IGNORE:C0103
        self.ui.setupUi(self)
        self.ui.material_table.setAlternatingRowColors(True)
        self.blueprints = None
        self.material_categories = None
        self.populate_blueprints()
        self.populate_skill_combo()
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
        self.blueprints = dict()
        for row in cursor:
            self.blueprints[row["typeName"]] = (row["typeID"])
        self.ui.blueprint_combo.addItems(self.blueprints.keys())
        self.ui.blueprint_combo.setEditText("")
        QtGui.QCompleter(self.blueprints.keys(), self.ui.blueprint_combo)
        self.ui.blueprint_combo.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        cursor.close()
        
    def populate_skill_combo(self):
        """
        Populates the skill selection combos with the available skill levels
        """
        skill_levels = ["N", "I", "II", "III", "IV", "V"]
        self.ui.pe_skill_combo.addItems(skill_levels)
        
    def populate_materials(self):
        """Populates the material tree view"""
        if str(self.ui.blueprint_combo.currentText()) != str():
            blueprint = get_blueprint(self.blueprints[str(self.ui.blueprint_combo.currentText())])
            materials = blueprint.get_bp_calc_materials(int(self.ui.me_spin.text()),
                                  int(self.ui.runs_spin.text()),
                                  roman.from_roman(self.ui.pe_skill_combo.currentText()))
            self.ui.material_table.clear()
            self.material_categories = list()
            minerals = QtGui.QTreeWidgetItem(self.ui.material_table,
                                             ["Minerals"])
            minerals.setExpanded(True)
            for material in materials:
                QtGui.QTreeWidgetItem(minerals, [material[0], material[1],
                                                 material[2], material[3],
                                                 "0", "0", material[4], "0"])
