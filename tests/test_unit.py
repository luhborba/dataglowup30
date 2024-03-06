import os
import sys

import duckdb
import pytest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)  # Adiciona o diretório raiz ao caminho do sistema

from etl.charge_init_db import load_csv_charge_duckdb


def test_duckdb_connection():
    # Estabelece uma conexão com o banco de dados DuckDB temporário para os testes
    conn = duckdb.connect(database="duckdb.db", read_only=False)
    assert conn is not None, "Failed to establish connection to DuckDB"
    conn.close()


def test_load_csv_charge_duckdb():
    # Define o caminho do arquivo de teste
    test_data_path = "test_data/"
    table_name = "teste"

    # Executa a função alvo
    load_csv_charge_duckdb(test_data_path, table_name)

    # Verifica se a tabela foi criada corretamente
    conn = duckdb.connect(database="duckdb.db", read_only=False)
    result = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
    assert result == 3  # Supondo que existam 3 linhas no arquivo de teste

    # Verifica se a tabela foi preenchida corretamente
    result = conn.execute(f"SELECT * FROM {table_name}").fetchone()
    assert len(result) == 3  # Supondo que existam 3 linhas no arquivo de teste
