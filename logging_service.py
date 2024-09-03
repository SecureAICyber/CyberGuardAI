import logging

class LoggingService:
    def __init__(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s [%(levelname)s] %(message)s',
                            handlers=[logging.FileHandler("debug.log"),
                                      logging.StreamHandler()])

    def log_info(self, msg):
        logging.info(msg)

    def log_error(self, msg):
        logging.error(msg)
