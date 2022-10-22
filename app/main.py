from fastapi import FastAPI;
from fastapi.middleware.cors import CORSMiddleware;
from .routers import youtube;

app = FastAPI ();

app.add_middleware (
  CORSMiddleware,
  allow_origins=['https://www.google.com'],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
);

app.include_router (youtube.router);