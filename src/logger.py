import logging
import os
from datetime import datetime

class CustomLog:

    def get_log(self):
        
        # log path is getting ready
        LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
        os.makedirs(logs_path, exist_ok=True)
        LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

        self.logger = logging.getLogger()
        self.file = str(LOG_FILE_PATH)
        self.logger.setLevel(logging.INFO)
        self.level = logging.INFO

        # Creating Formatters
        self.format = logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")
        
        # Creating Handlers
        self.file_handler = logging.FileHandler(LOG_FILE_PATH)


        # Adding Formatters to Handlers
        self.file_handler.setFormatter(self.format)

        # Adding Handlers to logger
        self.logger.addHandler(self.file_handler)

        return self.logger

def get_log_object():
    obj = CustomLog()
    log = obj.get_log()
    return log
 