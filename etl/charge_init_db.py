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
    Esta função carrega os arquivos da pasta `path`, transforma-os em um único DataFrame e o retorna.
    
    args:
        path (str): Caminho da pasta de arquivos.
    """
    # Conexão com o DuckDB
    con = duckdb.connect(database='duckdb.db', read_only=False)
    
    # Excluindo a tabela se existir
    con.execute("DROP TABLE IF EXISTS ecomerce_events")
    
    # Retornando o DataFrame do sql gerado no con.sql
    query = f'''SELECT * FROM "{path}/*.csv"'''
    
    # Criando tabela no banco duckdb, criado na variavel 'con' de acordo com a variavel 'query'
    con.execute(f' CREATE TABLE ecomerce_events AS {query}')

    # Fechando a conexão com o DuckDB
    con.close()
    
@log_decorator
@time_measure_decorator
def carregando_arquivos(path: str) -> List[pd.DataFrame]:
    """
    Esta função deve carregar os arquivos presentes na pasta data, transformar em uma lista de dataframes, concatena-los e retornar em um unico arquivo
    """
    arquivos = glob.glob(os.path.join(path, '*.csv'))
    list_df = []
    
    for arquivo in arquivos:
        list_df.append(pd.read_csv(arquivo))

    # concatenando Lista de DataFrames
    df = pd.concat(list_df)
    
    # salvando DataFrame em um arquivo
    df.to_csv('data.csv', index=False)
    
if __name__ == "__main__":
    path = "data/"
    df = load_csv_charge_duckdb(path)
    lista = carregando_arquivos(path)


