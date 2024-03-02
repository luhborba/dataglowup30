from etl.extract import download_kaggle_dataset
from etl.charge_init_db import load_csv_charge_duckdb

# Parametros
dataset: str = "mkechinov/ecommerce-events-history-in-cosmetics-shop"
path: str = "data/"
table_name = "ecomerce_events"

# Baixando Arquivos do Kaggle
download_kaggle_dataset(dataset, path)
# Carregando Arquivos no DuckDB
load_csv_charge_duckdb(path, table_name)
