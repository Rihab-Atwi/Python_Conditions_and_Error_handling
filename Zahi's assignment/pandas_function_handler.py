import psycopg2
from lookups import ErrorHandling
from logging_handler import show_error_text
import pandas as pd

def pandas_function(dataframe, function_name, condition = None):
    result = None
    try:
        if function_name == "remove_duplicates":
            result = dataframe.drop_duplicates()
        elif function_name == "remove_nulls":
            result = dataframe.dropna()
        elif function_name== "get_shape":
            result = dataframe.shape
        elif function_name == "get_length":
            result = len(dataframe)
        elif function_name == "filter_rows" and condition is not None:
            result = dataframe[condition]
        else:
            raise Exception("Invalid pandas function name")
    except Exception as e:
        prefix = ErrorHandling.PANDAS_FUNCTION_ERROR.value
        suffix = str(e)
        show_error_text(prefix,suffix)
    finally:
        return result

