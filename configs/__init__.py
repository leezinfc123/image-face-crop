"""
 Author: Hieund
 Company: MobioVN
 Date created: 02/11/2021
"""
import os


class Mongo:
    DB = 'test_image'
    URI = "localhost:27017"
    COLLECTION = 'image_test'


class Folder:
    # parent_dir
    data_dir = "../../src/data"
    manual_directory = "/manual_images/"
    crop_directory = "/crop_images/"
