"""
 Author: Hieund
 Company: MobioVN
 Date created: 05/11/2021
"""
import json

from configs import Folder
from src.controller.process_folder import create_folder_save
from src.controller.process_image import save_image
from src.model.mongodb.image import ImageModel


class ImageController:
    @staticmethod
    def save_image(files, video_name):

        # folder parent save images manual
        parent_dir = Folder.data_dir + Folder.manual_directory
        try:
            # create folder data
            print('save_image:create_folder_save')
            create_folder_save(parent_dir, video_name)
        except Exception as e:
            print("crop_face_image error: {}".format(e))
            return "exist file image"

        current_number_image = ImageModel().count_by_query({'video_name': video_name})
        path = parent_dir + video_name
        for file in files:
            image_name = video_name + '_' + str(current_number_image)
            path = path + '/' + image_name
            save_image(file, path)
            ImageModel().save_image(video_name, image_name, path)

    @staticmethod
    def get_list_image(video_name):
        images = ImageModel().get_images(video_name)
        return images
