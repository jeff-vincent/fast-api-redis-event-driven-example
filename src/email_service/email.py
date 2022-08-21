import asyncio
import os
import smtplib
import ssl
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
                        # send_email(i)

def send_email(email, data):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = os.environ.get('SENDER_EMAIL')
    receiver_email = email
    password = os.environ.get('SENDER_EMAIL_PASSWORD')
    message = f'You are {data["distance_from_velocity"]} miles from Velocity.'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

if __name__ == '__main__':
        asyncio.run(reader())
