# Config a Logger

# importing module
import logging

# Create and configure logger
logging.basicConfig(
    filename="newfile.log", format="%(asctime)s %(message)s", filemode="w"
)

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
logger.debug("I am Debugging this code")
logging.warning("this is a warning")
