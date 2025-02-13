import streamlit as st
from src.utils.read_data import read_data_from_csv
from src.forms import PrincipalForm
from src.input_cell import InputCellString
import pandas as pd
from config import config

#########Ingest
kpi_data = {
    'KPI': [
        'KPI1', 'KPI2', 'KPI3', 'KPI4', 'KPI5', 'KPI6', 'KPI7', 'KPI8', 'KPI9', 'KPI10',
        'KPI11', 'KPI12', 'KPI13', 'KPI14', 'KPI15', 'KPI16', 'KPI17', 'KPI18', 'KPI19', 'KPI20'
    ],
    'Year-Month': ['202501'] * 20  # Same date for simplicity
}

df_kpi = pd.DataFrame(kpi_data)

#st.write(dataframe)
user_email = 'ariel.flores1@mx.nestle.com' #Change the Email to see diferent form options: ariel.flores1@mx.nestle.com and fernando.lerios1@mx.nestle.com

if user_email:
    # Normalize email to lower-case for matching
    email_normalized = user_email.strip().lower()
    
    pm = PrincipalForm(list_of_cells = config.access_data[email_normalized]['template'])
    dictionary = pm.show()
    datafame_input=pm.preview(dictionary=dictionary)
    out=pm.wirite(principal_datafram=df_kpi[config.access_data[email_normalized]['columns']],dataframe_input=datafame_input)
    st.write('los datos a escribir son:')
    st.table(out)
