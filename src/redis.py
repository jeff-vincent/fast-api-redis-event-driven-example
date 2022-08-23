import os
import aioredis

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')

redis = aioredis.from_url(f'redis://{REDIS_HOST}:{REDIS_PORT}')
psub = redis.pubsub()
pub = aioredis.Redis.from_url(f'redis://{REDIS_HOST}:{REDIS_PORT}', 
    decode_responses=True)
