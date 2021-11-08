"""
 Author: Hieund
 Company: MobioVN
 Date created: 16/09/2021
"""
import os

from PIL import Image
import io
import numpy as np

from configs import Folder
from src.controller.mtcnn_model import create_model

Model_MTCCN = create_model()


def get_bytes_value(image):
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()


def process_crop_face_image(image):
    img = np.array(image)
    result = Model_MTCCN.detect_faces(img)
    box = result[0].get('box')
    x, y, width, height = box[0], box[1], box[2], box[3]
    image_crop = image.crop((x, y, x+width, y+height))
    return image_crop


def crop_face_image(file):

    try:
        image_bytes = file.file.read()
        decode = io.BytesIO(image_bytes)
        image = Image.open(decode)
        image = process_crop_face_image(image)
    except Exception as e:
        print("crop_face_image error: {}".format(e))
        return "crop face image fail"
    return get_bytes_value(image)


def crop_face_image_2(file):

    try:
        image_bytes = file.file.read()
        decode = io.BytesIO(image_bytes)
        image = Image.open(decode)
        image = process_crop_face_image(image)
        return image
    except Exception as e:
        print("crop_face_image error: {}".format(e))
        return "crop face image fail"


def save_image_manual(file, folder_path, image_name):
    image_bytes = file.file.read()
    decode = io.BytesIO(image_bytes)
    image = Image.open(decode)
    try:
        os.chdir(Folder.local_path)
        os.chdir(folder_path)
        image.save(image_name, 'PNG')
    except Exception as e:
        print("save_image error: {}".format(e))
        return "save_image image fail"


def save_image_crop(image, video_name, image_name):
    try:
        os.chdir(Folder.local_path)
        parent_dir = Folder.data_dir + Folder.crop_directory
        os.chdir(parent_dir)
        os.chdir(video_name)
        image.save(image_name, 'PNG')
    except Exception as e:
        print("save_image error: {}".format(e))
        return "save_image image fail"
