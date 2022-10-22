from fastapi import FastAPI;
from fastapi.middleware.cors import CORSMiddleware;
from .routers import youtube;

app = FastAPI ();

app.add_middleware (
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
);



@app.get('/')
def downloadVideo ():
  return {"success": "Done"};

@app.get ('/add/{a}/{b}')  
def add (a: int, b: int):
  return {"result": (a + b) * 2};

app.include_router (youtube.router);
