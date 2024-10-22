import logging
import logging.config


logging.config.fileConfig("logging.conf")

# logging.basicConfig(
#     filename="configfileEg.log", format="%(asctime)s %(message)s", filemode="w"
# )
# create logger
logger = logging.getLogger("simpleExample")


logger.error("Lets see if it only allows warnings")
logger.debug("This is a debug message")
logger.info("This is an informational message")
logger.warning("This is a warning message")
