"""
 Author: Hieund
 Company: MobioVN
 Date created: 16/09/2021
"""
import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from controller.process_image import crop_face_image

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return Response(crop_face_image(file), status_code=200)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=3000, log_level="info")
