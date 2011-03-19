'''
Created on 9 Feb 2010

@author: FrederikNS
'''

class Blueprint(object):
    '''
    classdocs
    '''
    def __init__(self, blueprint_type_id, runs=None, material_efficiency=None,
                 production_efficiency=None):
        '''
        Constructor
        '''
        self.blueprint_type_id = blueprint_type_id
        self.runs = runs
        self.material_efficiency = material_efficiency
        self.production_efficiency = production_efficiency
        
        """Should only be referenced directly by get_blueprint_type()"""
        self._blueprint = None
        
    def get_blueprint_type(self):
        """Populates and returns the _blueprint object"""
        if self._blueprint is None:
            from model.static.inv.blueprint_type import BlueprintType
            self._blueprint = BlueprintType(self.blueprint_type_id)
        return self._blueprint
    
    def get_parent_blueprint_type(self):
        return self.get_blueprint_type().get_parent_blueprint_type()
    
    def get_type(self):
        return self.get_blueprint_type().get_type()
    
    def get_product_type(self):
        return self.get_blueprint_type().get_product_type()
        
    def get_material_requirements(self):
        """Returns the materials object"""
        return self.get_blueprint_type().get_material_requirements()
    
    def get_requirements(self):
        """Returns the requirements object"""
        return self.get_blueprint_type().get_requirements()
    
    def get_material_base(self):
        """Returns the base amounts for manufacturing"""
        return self.get_blueprint_type().get_base_amounts()
    
    def get_material_waste(self, production_efficiency_skill,
        material_multiplier=1.0):
        """Returns the waste amounts for manufacturing"""
        return self.get_blueprint_type().get_waste(self.material_efficiency,
            production_efficiency_skill, material_multiplier)
    
    def get_material_totals(self, production_efficiency_skill,
        material_multiplier=1.0):
        """Returns the total amounts for manufacturing"""
        return self.get_blueprint_type().get_totals(self.material_efficiency,
            production_efficiency_skill, material_multiplier)
    
    def get_eliminate_waste(self):
        """Returns the eliminate waste levels for manufacturing"""
        return self.get_blueprint_type().get_eliminate_waste()
    
    def get_next_improvement(self, production_efficiency_skill,
        material_multiplier):
        """Returns the next improving level for me research"""
        return self.get_blueprint_type().get_next_improvement(
            self.material_efficiency, production_efficiency_skill,
            material_multiplier)
        
    def get_component_blueprints(self):
        return self.get_blueprint_type().get_component_blueprints()