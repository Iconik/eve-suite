from PySide import QtGui, QtCore
from view.blueprintcalculator.ui_blueprint_calculator import \
Ui_BlueprintCalculator
from viewmodel.blueprintcalculator.blueprint_calculator import \
BlueprintCalculator

class BlueprintDelegate(QtGui.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        if index.column() == 1 or index.column() == 2:
            editor = QtGui.QSpinBox(parent)
            editor.setRange(-2147483648,2147483647)
            #editor.editingFinished.connect(self.emitCommitData)
            return editor

    def setEditorData(self, editor, index):
        if index.column() == 1 or index.column() == 2:
            value = index.model().data(index, QtCore.Qt.SizeHintRole)
            if value is not None:
                editor.setValue(int(value))

    def setModelData(self, spinBox, model, index):
        if index.column() == 1 or index.column() == 2:
            spinBox.interpretText()
            value = spinBox.value()
            model.setData(index, value, QtCore.Qt.SizeHintRole)

class BlueprintCalculatorView(QtGui.QMainWindow):
    def __init__(self, parent=None):
        #Initialization
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_BlueprintCalculator()
        self.ui.setupUi(self)

        #Reference to the viewmodel
        self.bpc = BlueprintCalculator()

        #Setting up the combobox for selecting active blueprints, along with
        #suggestions
        self.ui.blueprint_combo.addItems(BlueprintCalculator.blueprint_list)
        self.ui.blueprint_combo.clearEditText()
        bpcompleter = QtGui.QCompleter(BlueprintCalculator.blueprint_list,
            self.ui.blueprint_combo)
        bpcompleter.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.blueprint_combo.setCompleter(bpcompleter)

        #Setting up material_tree
        self.ui.manufacturing_tree.setModel(self.bpc.material_model)
        self.ui.manufacturing_tree.setUniformRowHeights(True)
        for x in range(self.bpc.material_model.columnCount()):
            self.ui.manufacturing_tree.resizeColumnToContents(x)

        #Setting up blueprint_tree
        self.ui.blueprint_tree.setModel(self.bpc.blueprint_model)
        self.ui.blueprint_tree.setSelectionMode(
            QtGui.QAbstractItemView.NoSelection)
        self.ui.blueprint_tree.setItemDelegate(BlueprintDelegate(self))
        self.ui.blueprint_tree.setColumnWidth(1, 67)
        self.ui.blueprint_tree.setColumnWidth(2, 67)
        self.ui.blueprint_tree.setUniformRowHeights(True)
        self.ui.blueprint_tree.header()

        #Setting up actions
        self.ui.blueprint_combo.currentIndexChanged.connect(
            self.update_blueprints)

    def update_blueprints(self):
        self.bpc.blueprint_change(BlueprintCalculator.blueprint_dict[
            self.ui.blueprint_combo.itemText(
                self.ui.blueprint_combo.currentIndex())])
        for item in self.bpc.me_items:
            self.ui.blueprint_tree.openPersistentEditor(item.index())
        for item in self.bpc.pe_items:
            self.ui.blueprint_tree.openPersistentEditor(item.index())
        self.ui.blueprint_tree.expandAll()
        self.ui.blueprint_tree.resizeColumnToContents(0)
