import sqlite3
import pandas as pd

def get_column(database_name:str,
               table_name:str,
               column:str) -> dict:
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    
    consulta=f'SELECT {column} FROM {table_name}'
    
    df= pd.read_sql_query(consulta,conn)
    
    conn.close()
    return df
