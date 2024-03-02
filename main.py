from etl.extract import download_kaggle_dataset

dataset_name: str = "mkechinov/ecommerce-events-history-in-cosmetics-shop"
download_path: str = "data"


download_kaggle_dataset(dataset_name, download_path)