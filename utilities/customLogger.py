# import logging
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename='.\\Logs\\ automation.log',
#                             format='%(asctime)s: %(levelname)s: %(message)s',
#                             datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger

import logging

class LogGen:
    @staticmethod
    def loggen():
        # logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger


