import pymongo
import os

MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = os.environ.get('MONGO_PORT')

# TODO: define Redis consumer / publish email to Redis

conn_str = f'mongodb://{MONGO_HOST}:{MONGO_PORT}'
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client.example_db
users = db.users

# TODO: define consumer that listens to distance channel / calls insert_into_mongo(data)

def insert_into_mongo(data):
    users.insert_one(data)
    # TODO: publish data['email'] to Redis channel `email`
