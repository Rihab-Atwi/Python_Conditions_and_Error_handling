import psycopg2
from lookups import ErrorHandling
from logging_handler import show_error_text
import pandas as pd
import os

def get_csv_files(folder_path):
    csv_files = []
    try:
        for filename in os.listdir(folder_path):
            if filename.endswith(".csv"):
                csv_files.append(filename)
    except Exception as e:
        prefix = ErrorHandling.GET_CSV_FILES_ERROR.value
        suffix = str(e)
        show_error_text(prefix,suffix)
    finally:
        return csv_files
    