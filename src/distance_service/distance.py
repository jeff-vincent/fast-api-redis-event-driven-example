import asyncio
import json
from geopy.distance import geodesic
from redis import psub, pub

async def reader():
    async with psub as p:
        await p.subscribe('raw_input')
        if p != None:
            while True:
                message = await p.get_message(ignore_subscribe_messages=True)
                await asyncio.sleep(0)
                if message != None:
                    data = json.loads(message['data'])
                    try:
                        cd = CalculateDistance(data)
                        cd.distance_from_velocity()
                        calculated_data = json.dumps({'email': data['email'],
                        'distance_from_velocity': cd.distance})
                        await pub.publish('calculated_distance', calculated_data)
                    except Exception as e:
                        print(str(e))
                        pass
       
class CalculateDistance:
    def __init__(self, data):
        self.input_lat = data['lat']
        self.input_long = data['long']
        self.velocity_lat = 32.068227
        self.velocity_long = 34.794876
        self.distance = None
       
    def distance_from_velocity(self):
        self.distance = geodesic(
            (self.input_lat, self.input_long), 
            (self.velocity_lat, self.velocity_long)).miles

if __name__ == '__main__':
        asyncio.run(reader())
