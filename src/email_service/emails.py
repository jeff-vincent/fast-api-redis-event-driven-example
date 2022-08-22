import asyncio
import logging
from redis import psub
from mongo import users

logging.basicConfig(filename='sent_emails',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

async def reader():
    async with psub as p:
        await p.subscribe('user:email')
        if p != None:
            while True:
                message = await p.get_message(ignore_subscribe_messages=True)
                await asyncio.sleep(0)
                if message != None:
                    email = ((message['data']).decode('utf-8'))
                    data_from_db = users.find({"email": email})
                    for i in data_from_db:
                        send_email(email, i)
                        
def send_email(email, data):
    logging.info(f'Email sent to: {email}; Message: You are {data["distance_from_velocity"]} miles from Velocity.')

if __name__ == '__main__':
        asyncio.run(reader())






