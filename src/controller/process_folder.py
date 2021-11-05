"""
 Author: Hieund
 Company: MobioVN
 Date created: 02/11/2021
"""
import os

# parent_dir
parent_dir = "../../src/data"
directory = "Nikhil"


def create_folder_save(folder_name):
    # Path
    try:
        path = os.path.join(parent_dir, folder_name)
        os.mkdir(path)
    except:
        return None

