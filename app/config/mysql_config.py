import os
import logging
from mysql.connector.aio import connect

MYSQL_CONFIG = {
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'host': os.getenv('MYSQL_HOST'),
    'database': os.getenv('MYSQL_DATABASE')
}

async def get_mysql_connection():
    try:
        logging.info("Connecting to MySQL")
        return await connect(**MYSQL_CONFIG)
    except Exception as e:
        raise e
        
