import pandas as pandas

arquivo = 'read-csv/NEW_Electric_Vehicle_Population_Data.csv'

dados = pandas.read_csv(arquivo)

print(dados.head())