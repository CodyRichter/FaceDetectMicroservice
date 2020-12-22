from concurrent.futures.thread import ThreadPoolExecutor

from pydantic import BaseSettings

import logging

logger = logging.getLogger("api")

class Settings(BaseSettings):
    ready_to_predict = False


model_settings = Settings()


class PredictionException(Exception):
    pass


connected = False
shutdown = False
pool = ThreadPoolExecutor(10)
WAIT_TIME = 10
