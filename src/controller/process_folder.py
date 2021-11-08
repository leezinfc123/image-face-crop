"""
 Author: Hieund
 Company: MobioVN
 Date created: 02/11/2021
"""
import os
from builtins import print

from configs import Folder


def create_folder_save(parent_dir, folder_name):
    # Path
    try:
        # cd to local path
        os.chdir(Folder.local_path)
        os.chdir(parent_dir)
        os.mkdir(folder_name)
    except Exception as E:
        print('create_folder_save::error {}'.format(E))
        return None

