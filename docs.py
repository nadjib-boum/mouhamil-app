from fastapi import FastAPI;
from fastapi.params import Body;
from yt_dlp import YoutubeDL;
from .routers import youtube;




app = FastAPI ();


@app.get("/")
async def get_data (paramTes, otherParam):
  print (paramTest, otherParam); # ?paramtest=...&otherParam=....
  return {"msg": "Done"};

  
@app.post("/")
async def get_data (payload: dict = Body (...)):
  print (payload);
  return {"msg": "Done"};

@app.post("/data/{id}")
async def get_data (id):
  print (id);
  return {"msg": "Done", "payload": id};

app.include_router (youtube.router);