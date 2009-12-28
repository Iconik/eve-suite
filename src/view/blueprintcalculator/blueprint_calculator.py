from model.static.inventory.type import Type
from PyQt4 import QtGui

from view.blueprintcalculator.blueprint_calculator_template import Ui_MainWindow

from model.static.database import database
from model.static.inventory.blueprint_type import BlueprintType

class BlueprintCalculator(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.populate_blueprints()
        self.populate_skill_combo()
        
    def populate_blueprints(self):
        cursor = database.get_cursor("SELECT typeName FROM invBlueprintTypes LEFT JOIN invTypes ON blueprintTypeID=typeID WHERE published=1 ORDER BY typeName")
        self.blueprints = list()
        for row in cursor:
            self.blueprints.append(row[0])
        self.ui.comboBluprintSelection.addItems(self.blueprints)
        self.ui.comboBluprintSelection.setEditText("")
        QtGui.QCompleter(self.blueprints,self.ui.comboBluprintSelection)
        self.ui.comboBluprintSelection.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        cursor.close()
        
    def populate_skill_combo(self):
        skillLevels = ["I","II","III","IV","V"]
        self.ui.comboIndustry.addItems(skillLevels)
        self.ui.comboMetallurgy.addItems(skillLevels)
        self.ui.comboProductionEfficiency.addItems(skillLevels)
        self.ui.comboResearch.addItems(skillLevels)
        
    def populate_materials(self):
        type = Type(str(self.ui.comboBluprintSelection.currentText()))
        blueprint = BlueprintType(type)