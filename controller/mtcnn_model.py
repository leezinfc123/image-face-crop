"""
 Author: Hieund
 Company: MobioVN
 Date created: 16/09/2021
"""
from mtcnn import MTCNN


def create_model():
    detector_model = MTCNN()
    print("create model")
    return detector_model
