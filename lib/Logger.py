import logging

# -- TODO: Define loggers, handlers and filters. Appropriately implement logging module
class Logger:
    def __init__(self, loggername, loglevel):
        self.name = loggername
        loglevel = getattr(logging, loglevel.upper(), None)
        logging.basicConfig(format=f"%(asctime)s %(levelname)s: %(message)s", filename=f"{self.name!s}.log",
                            level=loglevel, filemode="w", datefmt="%d/%m/%Y %H:%M:%S")

    def log(self, level, message):
        level = level.upper()
        logging.debug("Log function called in Logger")
        if level == "DEBUG":
            logging.debug(f"From: {self.name!s}: {message!s}")
            return
        if level == "INFO":
            logging.info(f"From: {self.name!s}: {message!s}")
            return
        if level == "WARNING":
            logging.warning(f"From: {self.name!s}: {message!s}")
            return
        if level == "ERROR":
            logging.error(f"From: {self.name!s}: {message!s}")
            return
        if level == "CRITICAL":
            logging.critical(f"From: {self.name!s}: {message!s}")
            return
        else:
            logging.warning(f"Unknown log level encountered. Level was {level!s}. Message was {message!s}")
            return
