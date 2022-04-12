import logging

# create ang configure logger
logging.basicConfig(filename='CT8.log', format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger('logger_Name')

logger.setLevel(logging.INFO)

logger.debug(" Your debug message ")
logger.info(" your info message")
logger.warning(" Your warning message")
logger.error("Your error message")
logger.critical("your critical message")
