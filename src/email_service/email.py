from redis import psub
import asyncio
import os
import aioredis
import pymongo
from redis import psub

MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = os.environ.get('MONGO_PORT')

pub = aioredis.Redis.from_url("redis://localhost", decode_responses=True)

conn_str = f'mongodb://{MONGO_HOST}:{MONGO_PORT}'
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
db = client.example_db
users = db.users

async def reader():
    async with psub as p:
        await p.subscribe('channel_3')
        if p != None:
            while True:
                message = await p.get_message(ignore_subscribe_messages=True)
                await asyncio.sleep(0)
                if message != None:
                    email = ((message['data']).decode('utf-8'))
                    print(f'data from redis: {email}')
                    data_from_db = users.find_one({"email": email})
                    print(f'data from mongo: {data_from_db}')
                    send_email(data_from_db)


def send_email(data):
    pass
    

if __name__ == '__main__':
        asyncio.run(reader())
