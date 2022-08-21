import json
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import uvicorn
import aioredis
from redis import psub

from index import index_view

app = FastAPI()
pub = aioredis.Redis.from_url("redis://localhost", decode_responses=True)

@app.get("/")
async def index():
    return HTMLResponse(content=index_view, status_code=200)

@app.post("/distance")
async def login(email: str = Form(), 
lat: str = Form(), 
long: str = Form()):
    # TODO: publish to Redis
    data = {'email': email, 'lat': lat, 'long': long}
    r = await pub.publish('channel_1', json.dumps(data))
    
    return str(r)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
