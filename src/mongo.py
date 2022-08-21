import os
import pymongo

MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = os.environ.get('MONGO_PORT')

conn_str = f'mongodb://{MONGO_HOST}:{MONGO_PORT}'
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client.example_db
users = db.users