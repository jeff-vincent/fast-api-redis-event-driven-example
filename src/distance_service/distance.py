import asyncio
import json
import aioredis
from geopy.distance import geodesic
from redis import psub

pub = aioredis.Redis.from_url("redis://localhost", decode_responses=True)

async def reader():
    async with psub as p:
        await p.subscribe('channel_1')
        if p != None:
            while True:
                message = await p.get_message(ignore_subscribe_messages=True)
                await asyncio.sleep(0)
                if message != None:
                    data = json.loads(message['data'])
                    cd = CalculateDistance(data)
                    cd.distance_from_velocity()
                    calculated_data = json.dumps({'email': data['email'],
                    'distance_from_velocity': cd.distance})
                    print(calculated_data)
                    r = await pub.publish('channel_2', calculated_data)
                    print(r)
       
class CalculateDistance:
    def __init__(self, data):
        self.input_lat = data['lat']
        self.input_long = data['long']
        self.velocity_lat = 32.080058
        self.velocity_long = 34.864535
        self.distance = None
       
    def distance_from_velocity(self):
        self.distance = geodesic(
            (self.input_lat, self.input_long), 
            (self.velocity_lat, self.velocity_long)).miles

if __name__ == '__main__':
        asyncio.run(reader())
