"""
 Author: Hieund
 Company: MobioVN
 Date created: 02/11/2021
"""
import os

from configs import Folder


def create_folder_save(parent_dir, folder_name):
    # Path
    try:
        path = os.path.join(parent_dir, str(folder_name))
        print("/////////////////////////")
        print(path)
        os.mkdir(path)
    except Exception as e:
        print('create_folder_save::error {}'.format(e))
        return None


if __name__ == '__main__':
    parent_dir = Folder.data_dir + Folder.manual_directory
    try:
        # create folder data
        print('save_image:create_folder_save')
        create_folder_save(parent_dir, '123123')
    except Exception as e:
        print("crop_face_image error: {}".format(e))


