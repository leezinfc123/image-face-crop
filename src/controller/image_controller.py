"""
 Author: Hieund
 Company: MobioVN
 Date created: 05/11/2021
"""
import json

from src.model.mongodb.image import ImageModel


class ImageController:
    @staticmethod
    def save_image(files, video_name):
        for file in files:
            image_bytes = file.file.read()
            file_name = file.filename
            ImageModel().save_image(video_name, file_name, image_bytes)

    @staticmethod
    def get_list_image(video_name):
        images = ImageModel().get_images(video_name)
        return images
