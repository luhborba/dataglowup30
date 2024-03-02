from etl.extract import download_kaggle_dataset
from etl.charge_init_db import carregando_arquivos, load_csv_charge_duckdb

# Parametros
dataset: str = "mkechinov/ecommerce-events-history-in-cosmetics-shop"
path: str = "data/"

# Baixando Arquivos do Kaggle
download_kaggle_dataset(dataset, path)
# Carregando Arquivos no DuckDB
load_csv_charge_duckdb(path)
# Carregando Arquivo em formato no pandas
carregando_arquivos(path)