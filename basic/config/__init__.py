# Imports the Google Cloud client library
import os
from google.cloud import logging

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './temp.json'

# Instantiates a client
logging_client = logging.Client()

# The name of the log to write to
log_name = 'my-log'
# Selects the log to write to
logger = logging_client.logger(log_name)