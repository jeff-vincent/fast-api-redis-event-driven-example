import asyncio
from redis import psub
from mongo import users

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
                    data_from_db = users.find({"email": email})
                    for i in data_from_db:
                        print(f'data from mongo: {i}')
                    send_email(data_from_db)

def send_email(data):
    pass

if __name__ == '__main__':
        asyncio.run(reader())
