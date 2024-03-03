import time
from functools import wraps
from sys import stderr

from loguru import logger

logger.remove()

logger.add(
    sink=stderr, format="{time} <r>{level}</r> <g>{message}</g> {file}", level="INFO"
)

logger.add("log/etl.log", format="{time} {level} {message} {file}", level="INFO")

logger.add("log/etl.log", format="{time} {level} {message} {file}", level="CRITICAL")


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if func.__name__ != "extrair_dado":
            logger.info(f"Chamando função '{func.__name__}'")
            try:
                result = func(*args, **kwargs)
                logger.info(f"Função '{func.__name__}' executada com sucesso")
                return result
            except Exception as e:
                logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
                raise
        else:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
                raise

    return wrapper


def time_measure_decorator(func):
    """
    Função decoradora para medir o tempo de execução da função de entrada.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(
            f"Função '{func.__name__}' executada em {end_time - start_time:.4f} segundos"
        )
        return result

    return wrapper
