import psycopg2
from lookups import ErrorHandling, InputTypes
from logging_handler import show_error_text
import pandas as pd

config_dict = {
    "database": "NewDataBase",
    "host":"localhost",
    "port":5432,
    "user":"postgres",
    "password": "1234"
}

def create_connection():
    db_session = None
    try:
        db_session = psycopg2.connect(**config_dict)
    except Exception as e:
        prefix = ErrorHandling.DB_CONNECT_ERROR.value
        suffix = str(e)
        show_error_text(prefix, suffix)
    finally:
        return db_session
    
def return_query(db_session, query):
    results = None
    try:
        cursor = db_session.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        db_session.commit()
    except Exception as e:
        prefix = ErrorHandling.DB_RETURN_QUERY_ERROR.value
        suffix = str(e)
        show_error_text(prefix, suffix)
    finally:
        return results

def return_data_as_df(file, input_type, db_session=None):
    return_dataframe = None
    try:
        if input_type == InputTypes.CSV:
            return_dataframe = pd.read_csv(file)
        elif input_type == InputTypes.EXCEL:
            return_dataframe = pd.read_excel(file)
        elif input_type == InputTypes.SQL:
            return_dataframe = pd.read_sql_query(con=db_session, sql=file)
        else:
            raise Exception("The file type does not exist, please check main function")
    except Exception as e:
        suffix = str(e)
        if input_type == InputTypes.CSV:
            prefix = ErrorHandling.RETURN_DATA_CSV_ERROR.value
        elif input_type == InputTypes.EXCEL:
            prefix = ErrorHandling.RETURN_DATA_EXCEL_ERROR.value
        elif input_type == InputTypes.SQL:
            prefix = ErrorHandling.RETURN_DATA_SQL_ERROR.value
        else:
            prefix = ErrorHandling.RETURN_DATA_UNDEFINED_ERROR.value
        show_error_text(prefix, suffix)
    finally:
        return return_dataframe

def execute_query(db_session, query):
    try:
        cursor = db_session.cursor()
        cursor.execute(query)
        db_session.commit()
    except Exception as e:
        prefix = ErrorHandling.DB_EXECUTE_QUERY_ERROR.value
        suffix = str(e)
        show_error_text(prefix, suffix)

def get_tables_in_schema(db_session, schema_name):
    try:
        cursor = db_session.cursor()
        query = f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{schema_name}' AND table_type = 'BASE TABLE'"
        cursor.execute(query)
        table_names = cursor.fetchall()
        db_session.commit()
        return [table[0] for table in table_names]
    except Exception as e:
        prefix = ErrorHandling.DB_SCHEMA_INFO_ERROR.value
        suffix = str(e)
        show_error_text(prefix, suffix)