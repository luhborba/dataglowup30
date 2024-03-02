import os
import duckdb
import glob
import pandas as pd
from typing import List

from decorators.utils_decorators import log_decorator, time_measure_decorator

@log_decorator
@time_measure_decorator
def load_csv_charge_duckdb(path: str) -> pd.DataFrame:
    """
    Esta função carrega os arquivos da pasta `path` e insere no banco de dados.
    
    args:
        path (str): Caminho da pasta de arquivos.
    """
    # Conexão com o DuckDB
    con = duckdb.connect(database='duckdb.db', read_only=False)
    
    # Excluindo a tabela se existir
    con.execute("DROP TABLE IF EXISTS ecomerce_events")
    
    # Select dos arquivos CSV
    query = f'''SELECT * FROM "{path}/*.csv"'''
    
    # Criando tabela no banco duckdb, criado na variavel 'con' de acordo com a variavel 'query'
    con.execute(f' CREATE TABLE ecomerce_events AS {query}')

    # Fechando a conexão com o DuckDB
    con.close()
    
    
if __name__ == "__main__":
    path = "data/"
    load_csv_charge_duckdb(path)
  


