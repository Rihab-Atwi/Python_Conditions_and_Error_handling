from enum import Enum
class ErrorHandling(Enum):
    DB_CONNECT_ERROR = "DB Connect Error"
    DB_RETURN_QUERY_ERROR = "DB Return Query Error"
    API_ERROR = "Error calling API"
    RETURN_DATA_CSV_ERROR = "Error returning CSV"
    RETURN_DATA_EXCEL_ERROR = "Error returning Excel"
    RETURN_DATA_SQL_ERROR = "Error returning SQL"
    RETURN_DATA_UNDEFINED_ERROR = "Cannot find File type"
    DB_EXECUTE_QUERY_ERROR = "DB Execute Query Error" #New
    PANDAS_FUNCTION_ERROR = "Pandas Function Error"  #New
    GET_CSV_FILES_ERROR = "Get CSV Files Error"      #New
    DB_SCHEMA_INFO_ERROR = "DB Schema Info Error"    #New


class InputTypes(Enum):
    SQL = "SQL"
    CSV = "CSV"
    EXCEL = "Excel"