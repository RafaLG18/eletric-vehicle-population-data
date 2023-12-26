from create_a_database.create_db import create_db
from create_tables.create_tables import create_table
from read_csv.read_csv import read
from fill_table.fill import fill

def main():
    # Creating database
    create_db("eletric_cars.db")

    # Creating tables
    create_table(database_name="eletric_cars.db",table_name="address",
                 columns="""
                 id_address INTEGER PRIMARY KEY AUTOINCREMENT,
                 county TEXT,
                 city TEXT,
                 state TEXT,
                 postalCode INT
                 """
                 )
    create_table(database_name="eletric_cars.db",table_name="vehicle_data",
                 columns="""
                 id_vehicle_data INTEGER PRIMARY KEY AUTOINCREMENT,
                 vin TEXT,
                 modelYear INTEGER NOT NULL,
                 make TEXT,
                 model TEXT
                 """
                 )
    create_table(database_name="eletric_cars.db",table_name="electric_vehicle",
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
    fill("eletric_cars.db",df)

if __name__ == "__main__":
    main()
