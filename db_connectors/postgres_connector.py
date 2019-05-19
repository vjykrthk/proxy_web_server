from venv import logger

import psycopg2


class PostgresConnector:
    def __init__(self):
        # I have simplified here. In real application I will be constructing the url
        # from environment variables. Also postgres could be running in a docker container
        connect_str = "dbname='proxy_server' user='karthik' host='localhost' password='myOwnPassword'"

        self.conn = psycopg2.connect(connect_str)
        self.cursor = self.conn.cursor()

    def close_client(self):
        self.cursor.close()
        self.conn.close()

    def execute(self, query):
        result = self.cursor.execute(query)
        self.conn.commit()
        logger.info('Executing Query - {query} Result - {result}'.format(query=query, result=result))
        return result
