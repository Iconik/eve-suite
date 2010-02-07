'''
Created on 23 Dec 2009

@author: FrederikNS
'''
from model.static.database import database
from model.dynamic.inventory.item import Item
import math

class TypeMaterials(object):
    """
     # PyUML: Do not remove this line! # XMI_ID:_EIHDIBEREd-LgJ4IxcJkTA
    """

    def __init__(self,
                 type_id):
        '''
        Constructor
        '''
        self.type_id = type_id
        self.materials = list()
        cursor = database.get_cursor("select typeID, materialTypeID, quantity \
        from invTypeMaterials where typeID=%s;" % (self.type_id))
        
        for row in cursor:
            self.materials.append(Item(row["materialTypeID"],
                                       quantity=row["quantity"]))
        
    def get_material_calc(self, material_efficiency, runs, pe_skill,
                          waste_factor):
        """
        Calculates the materials for the given parameters, and returns them
        """
        materials = list()
        for material in self.materials:
            name = material.get_type().type_name
            
            base_amount = material.quantity
            
            if material_efficiency >= 0:
                waste = int(round(float(material.quantity) *
                             ((float(waste_factor) / 100) *
                              (1 / float(material_efficiency + 1)) +
                              (5 - pe_skill) * 0.05)))
            else:
                waste = int(round(float(material.quantity) *
                             ((float(waste_factor) / 100) *
                              (1 - material_efficiency) +
                              (5 - pe_skill) * 0.05)))
            
            perfect_me = int(math.ceil(0.02*waste_factor*material.quantity))
            
            materials.append([name, str(base_amount*runs), str(waste*runs),
                              str(base_amount*runs+waste*runs), 
                              str(perfect_me)])
        return materials
