import sqlite3

def create_db(database_name:str):
    """Create a database

    Args:
        database_name (str): Eletric_Vehicle_Population
    """
    sqlite3.connect(database_name)