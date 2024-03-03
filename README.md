# Desafio DataGlowUp do Mestre Heitor Sasaki de nº 30 [Em desenvolvimento]

A ideia do projeto é realizar um processo ETL completo utilizando das melhores boas práticas, considerando os dados disponibilizados pelo Mestre Heitor.

Siga o Mestre Heitor:
[Linkedin do Mestre](https://www.linkedin.com/in/heitorsasaki/)

DataSet Utilizado
[Dados no Kaggle](https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-cosmetics-shop)

## Stack Utilizada [Até o momento]

- Python
- Pyenv
- Poetry
- DuckDB
- Pytest
- Black
- Loguru

## Ações Realizadas

Até o momento, foi realizada a extração dos dados via API do Kaggle e depois realizado a carga destes dados para um banco utilizando o `DuckDB`, como também realizados testes utilizando a biblioteca `pytest`, além de estar utilizando funções decoradoras para realização de logs (Utilizando a biblioteca `loguru`) e de contabilização de execução.

## Configuração do Computador Utilizado

- Processador: AMD Ryzen 3 5300U with Radeon Graphics 2.6 Ghz
- RAM: 8 GB DDR-4
- SSD Sata: 256 GB
- SO: Windows 11 23H2

## Clonando o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/luhborba/dataglowup30.git
cd dataglowup30
```

2. Configure a versão correta do Python com `pyenv`
```bash
pyenv install 3.12.1
pyenv local 3.12.1
```

3. Ativando Poetry
```bash
poetry env use 3.12.1
poetry shell
```

4. Insatalando dependências
```bash
poetry install
```
