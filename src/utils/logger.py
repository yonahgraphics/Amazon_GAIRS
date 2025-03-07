import logging
import os
from datetime import datetime
from config import Directory



logs_directory = Directory.LOGS.value

# Ensure logs directory exists
os.makedirs(logs_directory, exist_ok=True)

# Create a unique log file name with timestamp
timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
log_filename = f'{logs_directory}/app_{timestamp}.log'

# Configure the logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(f"{log_filename}"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
if __name__ == "__main__":
    logger.info("Application started")
    
    logger.info("Application finished")
