"""Arquivo que contem função de carregamento inicial do DuckDB."""
import duckdb

from decorators.utils_decorators import log_decorator, time_measure_decorator


@log_decorator
@time_measure_decorator
def load_csv_charge_duckdb(path: str, table_name: str):
    """
    Esta função carrega os arquivos da pasta `path` e insere no banco de dados.

    args:
        path (str): Caminho da pasta de arquivos.
        table_name (str): Nome da tabela no DuckDB.
    """
    # Conexão com o DuckDB
    con = duckdb.connect(database="duckdb.db", read_only=False)

    # Excluindo a tabela se existir
    con.execute(f"DROP TABLE IF EXISTS {table_name}")

    # Select dos arquivos CSV
    query = f'''SELECT * FROM "{path}/*.csv"'''

    # Criando tabela no banco duckdb, criado na variavel 'con' de acordo com a variavel 'query'
    con.execute(f" CREATE TABLE {table_name} AS {query}")

    # Fechando a conexão com o DuckDB
    con.close()


if __name__ == "__main__":
    path = "data/"
    table_name = "ecomerce_events"
    load_csv_charge_duckdb(path, table_name)
