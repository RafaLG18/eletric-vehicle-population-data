import sqlite3

def insert_one_row(
    database_name: str,
    table_name:str,
    columns_name:str,
    values: str) -> None:
    """ Create
       Args:
        database_name (str): created database name 
        table_name (str): table name 
        columns_name (str): A query specifying the columns
        values (str): Values to insert
        
       Example:
        insert_one_row(database_name="database.db",
               table_name="tabela_amada",
               columns_name="id,nome_flor,qtd_petala_flor",
               values="2,'copo_de_leite',3")
    """
    conn=sqlite3.connect(database_name)
    cursor=conn.cursor()
    cursor.execute(
        f"""
        INSERT INTO {table_name} ({columns_name}) VALUES ({values})
        """
    )
    conn.commit()
    conn.close()
    
def insert_many_rows(database_name: str,
    table_name:str,
    columns_name:str,
    list_values: list) -> None:
    """ Create
       Args:
        database_name (str): created database name 
        table_name (str): table name 
        columns_name (str): A query specifying the columns
        list_values (list): List of values to insert
        
       Example:
        insert_many_rows(database_name="database.db",
               table_name="tabela_amada",
               columns_name="id,nome_flor,qtd_petala_flor",
               list_values=[(9,'flor do deserto',4),(10,'flor do deserto',5),(11,'flor do deserto',6)])
    """
    
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    placeholders=','.join(['?' for _ in range(len(list_values[0]))])
    query=f"INSERT INTO {table_name} ({columns_name}) VALUES ({placeholders})"
    cursor.executemany(query,list_values)
    conn.commit()
    conn.close()
