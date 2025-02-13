
import pandas as pd
from typing import Dict
def transform_dictionary_to_pandas(dictionary:Dict)->pd.DataFrame:
    return pd.DataFrame(dictionary,index=[0])

