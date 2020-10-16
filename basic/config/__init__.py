# Imports the Google Cloud client library
import os
from google.cloud import logging

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './xyz.json'

logging_client = logging.Client()

# This log can be found in the Cloud Logging console under 'Custom Logs'.
logger = logging_client.logger("MyLogger")

# Make a simple text log
logger.log_text('Hello, world!', severity='INFO')

# Simple text log with severity.
logger.log_text('Goodbye, world!', severity='INFO')