import logging
import os

# Set up logging configuration
LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'DEBUG')
logging.basicConfig(
    filename='bot_operations.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=LOGGING_LEVEL,
)

# Example usage of the logger
logger = logging.getLogger(__name__)

# Log bot start
logger.info('Bot is starting...')

# Log example function

def execute_admin_operation(operation):
    logger.info(f'Admin operation executed: {operation}')
    # Add actual logic here

# Log bot stop
logger.info('Bot is shutting down...')
