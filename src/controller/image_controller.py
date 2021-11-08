"""
 Author: Hieund
 Company: MobioVN
 Date created: 05/11/2021
"""
import glob
import os

from PIL import Image

from configs import Folder
from src.controller.process_folder import create_folder_save
from src.controller.process_image import save_image_manual, process_crop_face_image, save_image_crop
from src.model.mongodb.image_crop import ImageCropModel
from src.model.mongodb.image_manual import ImageManualModel


class ImageController:
    @staticmethod
    def save_image(files, video_name):
        # folder parent save images manual
        parent_manual_dir = Folder.data_dir + Folder.manual_directory
        parent_crop_dir = Folder.data_dir + Folder.crop_directory
        try:
            # create folder data
            print('save_image:create_folder_save: {} -- {}'.format(parent_manual_dir, video_name))
            print('save_image:create_folder_save: {} -- {}'.format(parent_crop_dir, video_name))
            create_folder_save(parent_manual_dir, video_name)
            create_folder_save(parent_crop_dir, video_name)
        except Exception as e:
            print("crop_face_image error: {}".format(e))
            return "exist file image"

        current_number_image = ImageManualModel().count_by_query({'video_name': video_name})
        path = parent_manual_dir + video_name
        # save manual image
        for file in files:
            current_number_image += 1
            image_name = video_name + '_' + str(current_number_image) + '.png'
            save_image_manual(file, path, image_name)
            ImageManualModel().save_image(video_name, image_name, parent_manual_dir)

        ImageController.process_crop_face_image(video_name)

    @staticmethod
    def get_list_image(video_name):
        images = ImageManualModel().get_images(video_name)
        return {
            'data': list(images)
        }

    @staticmethod
    def process_crop_face_image(video_name):
        manual_image_path = Folder.data_dir + Folder.manual_directory
        os.chdir(Folder.local_path)
        os.chdir(manual_image_path)
        for filename in glob.glob('{}/*.png'.format(video_name)):
            image = Image.open(filename)
            image_name = filename.split('/')[1]
            print(image_name)
            try:
                image = process_crop_face_image(image)
                save_image_crop(image, video_name, image_name)
                ImageCropModel().save_image(video_name, image_name, manual_image_path)
            except Exception as e:
                print("crop_face_image error: {}".format(e))
                return "crop face image fail"


if __name__ == '__main__':
    ImageController.process_crop_face_image('hieu')
