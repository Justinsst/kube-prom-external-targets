import os
LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO')
NAMESPACE = os.environ.get('NAMESPACE', 'default')
REFRESH_INTERVAL = os.environ.get('REFRESH_INTERVAL', 60)
REQUEST_RETRIES = os.environ.get('REQUEST_RETRIES', 3)
RETRY_REQUEST_INTERVAL = os.environ.get('RETRY_REQUEST_INTERVAL', 5)
