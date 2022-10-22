from fastapi import APIRouter;
from yt_dlp import YoutubeDL;

router = APIRouter (prefix='/youtube', tags=['youtube']);

@router.get('/video')
def downloadVideo ():
  return {"msg": "youtube Router Done"};