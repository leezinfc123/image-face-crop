"""
 Author: Hieund
 Company: MobioVN
 Date created: 16/09/2021
"""
import uvicorn
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from src.controller.process_image import crop_face_image
from src.controller.image_controller import ImageController
from typing import List

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/crop-face-image/")
async def crop_image(file: UploadFile = File(...)):
    return Response(crop_face_image(file), status_code=200)


@app.post("/save-image/")
async def save_image(video_name: str = Form(...), images: List[UploadFile] = File(...)):
    return Response(ImageController.save_image(images, video_name), status_code=200)


@app.get("/list-image/")
async def get_list_image(video_name: str = ''):
    return Response(ImageController.get_list_image(video_name), status_code=200)


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=3000, log_level="info")
