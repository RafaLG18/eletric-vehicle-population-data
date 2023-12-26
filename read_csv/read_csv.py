import pandas as pandas

def read(file_path:str) -> dict:
    dados=pandas.read_csv(file_path)
    return dados