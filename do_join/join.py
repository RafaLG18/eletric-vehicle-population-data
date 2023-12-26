import sqlite3
from create_tables.create_tables import create_table

def join(database_name:str,
         table_name:str,
         columns:str,
         dataframe:str,
         index:str):
    
    create_table(database_name,table_name,columns)
    
    conn=sqlite3.connect(database_name)
    dataframe.to_sql(table_name, con=conn, index_label=index, if_exists='append')
    
    conn.commit()
    conn.close()

