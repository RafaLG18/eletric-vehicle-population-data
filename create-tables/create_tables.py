import sqlite3

def create_table(database_name:str,
                 table_name:str,
                 columns:str,
                ) -> None:
    """Create a table in a database previously created

    Args:
        database_name (str): created database name
        table_name (str): table name
        columns (str): columns' database
    """

    conn= sqlite3.connect(database_name)
    cursor=conn.cursor()

    cursor.execute(
        f'''
        CREATE TABLE IF NOT EXISTS {table_name} ({columns})
        '''
    )
    conn.close()