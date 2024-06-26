import logging
import time
import mysql.connector

logger = logging.getLogger(__name__)


# From: https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
def connect_to_mysql(config, attempts=3, delay=2):
    attempt = 1
    # Implement a reconnection routine
    while attempt < attempts + 1:
        try:
            return mysql.connector.connect(**config)
        except (mysql.connector.Error, IOError) as err:
            if attempts is attempt:
                # Attempts to reconnect failed; returning None
                logger.info(
                    'Failed to connect, exiting without a connection: %s', err
                )
                return None
            logger.info(
                'Connection failed: %s. Retrying (%d/%d)...',
                err,
                attempt,
                attempts - 1,
            )
            # progressive reconnect delay
            time.sleep(delay**attempt)
            attempt += 1
    return None
