"""Arquivo para extração dos dados."""
import os
import subprocess

from dotenv import load_dotenv

from decorators.utils_decorators import log_decorator, time_measure_decorator

load_dotenv()


@time_measure_decorator
@log_decorator
def download_kaggle_dataset(dataset_name: str, download_path: str):
    """
    Função tem como objetivo realizar o download de conjuntos do Kaglle, UTILIZANDO A api do Kaggle e salvando em um caminho especificado.

    Args:
        dataset_name (str): Nome do conjunto de dados do Kaggle (por exemplo, "mkechinov/ecommerce-events-history-in-cosmetics-shop").
        download_path (str): Caminho onde o arquivo do conjunto de dados deve ser salvo.
    """
    # Obtém as credenciais do Kaggle das variáveis de ambiente
    kaggle_username = os.getenv("KAGGLE_USERNAME")
    kaggle_key = os.getenv("KAGGLE_KEY")

    # Define as credenciais da API do Kaggle
    os.environ["KAGGLE_USERNAME"] = kaggle_username
    os.environ["KAGGLE_KEY"] = kaggle_key

    try:
        # Faz o download do conjunto de dados usando a API do Kaggle
        subprocess.run(
            [
                "kaggle",
                "datasets",
                "download",
                "-d",
                dataset_name,
                "-p",
                download_path,
                "--unzip",
            ],
            check=True,
        )
        print(
            f"O conjunto de dados {dataset_name} foi baixado e salvo como {download_path}."
        )
    except subprocess.CalledProcessError as e:
        print(f"Erro ao baixar o conjunto de dados: {e}")


if __name__ == "__main__":
    dataset_name: str = "mkechinov/ecommerce-events-history-in-cosmetics-shop"
    download_path: str = "data"
    download_kaggle_dataset(dataset_name, download_path)
