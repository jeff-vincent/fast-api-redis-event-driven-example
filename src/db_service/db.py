import asyncio
import json
import os
import aioredis
import pymongo
from redis import psub

MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = os.environ.get('MONGO_PORT')

pub = aioredis.Redis.from_url("redis://localhost", decode_responses=True)

# TODO: define Redis consumer / publish email to Redis

conn_str = f'mongodb://{MONGO_HOST}:{MONGO_PORT}'
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client.example_db
users = db.users

async def reader():
    async with psub as p:
        await p.subscribe('channel_2')
        if p != None:
            while True:
                message = await p.get_message(ignore_subscribe_messages=True)
                await asyncio.sleep(0)
                if message != None:
                    data = json.loads(message['data'])
                    insert_into_mongo(data)
                    r = await pub.publish('channel_3', data['email'])
                    print(r)


def insert_into_mongo(data):
    users.insert_one(data)

if __name__ == '__main__':
        asyncio.run(reader())
