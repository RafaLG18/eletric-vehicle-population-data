from create_a_database.create_db import create_db
from create_tables.create_tables import create_table
from read_csv.read_csv import read
from fill_table.fill import fill
from query.get_columns import get_column
from do_join.join import join
import pandas as pd
def main():
    # Creating database
    database="eletric_cars.db"
    
    create_db(database)

    # Creating tables
    create_table(database_name=database,table_name="address",
                 columns="""
                 id_address INTEGER PRIMARY KEY AUTOINCREMENT,
                 county TEXT,
                 city TEXT,
                 state TEXT,
                 postalCode INT
                 """
                 )
    create_table(database_name=database,table_name="vehicle_data",
                 columns="""
                 id_vehicle_data INTEGER PRIMARY KEY AUTOINCREMENT,
                 vin TEXT,
                 modelYear INTEGER NOT NULL,
                 make TEXT,
                 model TEXT
                 """
                 )
    create_table(database_name=database,table_name="electric_vehicle",
                 columns="""
                 id_electric_vehicle INTEGER PRIMARY KEY AUTOINCREMENT,
                 electricVehicleType TEXT,
                 electricRange TEXT,
                 legislativeDistrict TEXT,
                 electricUtility TEXT
                 """
                 )

    # Reading dataframe 
    df=read("electric_vehicle.csv")
    # Fill tables
    fill(database,df)
    
    # Building tables to join
    # build vehicle_localization_data
    df_vehicle_localization_data=pd.DataFrame(columns=['id_address','vin'])
    df_vehicle_localization_data["id_address"]=get_column(database_name=database,table_name="address",column="id_address")
    df_vehicle_localization_data["vin"]=get_column(database_name=database,table_name="vehicle_data",column="vin")
    join(database_name=database,
         table_name="vehicle_localization_data",
         columns="""
            id_vehicle_localization_data INTEGER PRIMARY KEY AUTOINCREMENT,
            id_address INT,
            vin TEXT
         """,
         dataframe=df_vehicle_localization_data,
         index="id_vehicle_localization_data")
    # build vehicle_eletric_data
    df_vehicle_eletric_data=pd.DataFrame(columns=['id_eletric_vehicle','vin'])
    df_vehicle_eletric_data["id_eletric_vehicle"]=get_column(database_name=database,table_name="electric_vehicle",column="id_electric_vehicle")
    df_vehicle_eletric_data["vin"]=get_column(database_name=database,table_name="vehicle_data",column="vin")
    join(database_name=database,
         table_name="vehicle_eletric_data",
         columns="""
            id_vehicle_eletric_data INTEGER PRIMARY KEY AUTOINCREMENT,
            id_eletric_vehicle INT,
            vin TEXT
         """,
         dataframe=df_vehicle_eletric_data,
         index="id_vehicle_eletric_data")
    
if __name__ == "__main__":
    main()
