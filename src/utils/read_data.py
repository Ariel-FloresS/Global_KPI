import pandas as pd
#from snowflake.snowpark.context import get_active_session

def read_data_from_csv(path)->pd.DataFrame:
    return pd.read_csv(path)

#def read_data_from_table(table_name)->pd.DataFrame:
#    session = get_active_session()
#    return session.table(table_name).to_pandas()
