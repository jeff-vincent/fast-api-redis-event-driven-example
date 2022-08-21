import json
from fastapi import FastAPI, Form, BackgroundTasks
from fastapi.responses import HTMLResponse
import uvicorn
from redis import pub

from index import index_view

app = FastAPI()

@app.get("/")
async def index():
    return HTMLResponse(content=index_view, status_code=200)

async def publish_to_redis(data: dict):
    await pub.publish('channel_1', json.dumps(data))

@app.post("/distance")
async def login(background_tasks: BackgroundTasks,
email: str = Form(), 
lat: str = Form(), 
long: str = Form()):
    data = {'email': email, 'lat': lat, 'long': long}
    background_tasks.add_task(publish_to_redis, data)
    
    return HTMLResponse(content=index_view, status_code=201)

# if __name__ == '__main__':
#     uvicorn.run(app, host="localhost", port=8000)
