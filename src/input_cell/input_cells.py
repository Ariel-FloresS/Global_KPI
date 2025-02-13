from ._abstract_input_cell import AbstractInputCell
import streamlit as st
from typing import Dict
import re


class InputCellString(AbstractInputCell):

    def __init__(self, cell_name:str, validate_dict:Dict={'Validate':False,'Patter':r"^KPI\d{1,}"})->None:

        self.cell_name = cell_name
        self.validate_dict = validate_dict

    def get_status_cell(self)->bool:
        return self.status_cell
    
    def input(self)->str:

        value = st.text_input(
                    label = self.cell_name,
                )
      
        if self.validate_dict['Validate']:
            if value:
                if not re.match(self.validate_dict['Patter'],value):
                    st.error(f" the input value: {value} ,is  not valid")   
                else:
                    self.status_cell = True
                    return value
        else:
            self.status_cell = True
            return value
        

class InputCellInt(AbstractInputCell):

    def __init__(self,cell_name:str, 
                 validate_dict:Dict={'Validate':False,'max':100,'min':0}
                 )->None:
      
        self.cell_name = cell_name
        #self.validate_dict = validate_dict
    def input(self)->int:
        
        if self.validate_dict['Validate']:
            value = st.number_input(
                    label = self.cell_name,
					min_value=self.validate_dict['min'],
					max_value=self.validate_dict['max']					
                )
            
            self.status_cell = True
            return value
        else:
            self.status_cell = True
            return value