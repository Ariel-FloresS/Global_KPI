from typing import List,Dict,Any
from src.input_cell import AbstractInputCell

from src.utils.transform import transform_dictionary_to_pandas
import streamlit as st
import pandas as pd
import time


class PrincipalForm:
    def __init__(self, list_of_cells:List[AbstractInputCell])->None:

        self.list_of_cells = list_of_cells
        self.sesion_state = st.session_state


    def show(self)->Dict[str,Any]:
        
        for cell in self.list_of_cells:
            st.write(f"Configuración para: {cell.cell_name}")
            cell.status_cell=False
          
            if not cell.status_cell:
                value = cell.input()
                st.write(f"El valor es: {value}")
           
            if cell.status_cell:
                self.sesion_state [cell.cell_name] = value
        return dict(self.sesion_state)
    
    def preview(self,dictionary:Dict)->pd.DataFrame:
         dataframe_to_snow = transform_dictionary_to_pandas(dictionary=dictionary)
         st.write('Preview de los datos a escribir.')   
         st.table(data=dataframe_to_snow)
         return dataframe_to_snow

    def wirite(self,principal_datafram:pd.DataFrame, dataframe_input:pd.DataFrame)->None:
        if st.button('Guardar los datos'):
            with st.spinner('Guardando datos'):
                 time.sleep(2)
                 concat_df =pd.concat([principal_datafram,dataframe_input]).drop_duplicates()
            st.success('Datos guardados con exito')
            return concat_df
         
            
         

    

        



                

                

                
        