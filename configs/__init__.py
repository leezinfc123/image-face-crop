"""
 Author: Hieund
 Company: MobioVN
 Date created: 02/11/2021
"""


class Mongo:
    DB = 'test_image'
    URI = "localhost:27017"
    COLLECTION = 'image_test'


class Folder:
    # path source code
    local_path = "/home/hieu/image-face-crop"
    # parent_dir
    data_dir = "./src/data"
    manual_directory = "/manual_images/"
    crop_directory = "/crop_images/"
