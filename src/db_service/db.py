import asyncio
import json
from redis import psub, pub
from mongo import users

async def reader():
    async with psub as p:
        await p.subscribe('calculated_distance')
        if p != None:
            while True:
                message = await p.get_message(ignore_subscribe_messages=True)
                await asyncio.sleep(0)
                if message != None:
                    data = json.loads(message['data'])
                    insert_into_mongo(data)
                    await pub.publish('user:email', data['email'])

def insert_into_mongo(data):
    users.insert_one(data)

if __name__ == '__main__':
        asyncio.run(reader())
