'''
Created on Jun 3, 2010

@author: frederikns
'''
from model.static.inv import inventory_dictionaries

class ManufactureWorkflow(object):
    def __init__(self,initial_type_id,material_level,production_level,runs,industry,metallurgy,production_efficiency,research):
        '''
        Constructor
        '''
        self.initial_type_id = initial_type_id
        self.material_level = material_level
        self.production_level = production_level
        self.runs = runs
        self.industry = industry
        self.metallurgy = metallurgy
        self.production_efficiency = production_efficiency
        self.research = research
        
        self.type = inventory_dictionaries.get_type(self.initial_type_id)
        