import sqlite3
# Fill tables with data
def fill(database_name:str,
         dataframe_name:str):
    """ Create
       Args:
        database_name (str): created database name 
        dataframe_name (str): created dataframe name
        
       Example:
        fill("eletric_cars.db",df)
    """
    # Connect with database 
    conn=sqlite3.connect(database_name)
    # Table as df
    df_adress=dataframe_name[["county","city","state","postalCode"]]
    df_vehicle_data=dataframe_name[["vin","modelYear","make","model"]]
    df_electric_vehicle=dataframe_name[["electricVehicleType","electricRange","legislativeDistrict","electricUtility"]]
    # Fill tables
    df_adress.to_sql('address', con=conn, index_label="id_address", if_exists='append')
    df_vehicle_data.to_sql('vehicle_data', con=conn, index_label="id_vehicle_data",if_exists='append')
    df_electric_vehicle.to_sql('electric_vehicle', con=conn, index_label="id_electric_vehicle", if_exists='append')
    conn.commit()
    conn.close()

