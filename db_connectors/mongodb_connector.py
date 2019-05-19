from venv import logger

from pymongo import MongoClient


class MongoDBConnector:
    def __init__(self, db_name):
        # I have simplified here. In real application I will be constructing the url
        # from environment variables
        client = MongoClient('mongodb://localhost:27017/')
        self.db = client[db_name]

    def insert_row(self, collection_name, row):
        result = self.db[collection_name].insert(row)
        logger.info('Insert row - {row} result - {result}'.format(row=row, result=result))
        return result

    def find(self, match, project, *args, **kwargs):
        pass
