'''
Created on 9 Feb 2010

@author: FrederikNS
'''

from model.static.inv import inventory_dictionaries

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
        
        self.blueprint = None
        
    def get_blueprint(self):
        if self.blueprint is None:
            self.blueprint = inventory_dictionaries.get_blueprint(
                self.blueprint_type_id)
        return self.blueprint
        
    def get_requirements(self):
        return self.get_blueprint().get_requirements()
    
    def get_materials(self):
        return self.get_blueprint().get_materials()
    
    def get_combined(self, production_efficiency_skill):
        return self.get_blueprint().get_combined(self.material_efficiency,
                                          production_efficiency_skill)
        
    def get_production_times(self):
        pass