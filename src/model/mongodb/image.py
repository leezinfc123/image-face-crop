"""
 Author: Hieund
 Company: MobioVN
 Date created: 05/11/2021
"""
import datetime

from mongoengine import Document, StringField, DateTimeField, IntField
from src.model.mongodb import BaseModel


class ImageModel(BaseModel, Document):
    video_name = StringField()
    image_name = StringField()
    data = StringField()
    created_time = DateTimeField()
    priority = IntField()

    def __init__(self, *args, **values):
        super().__init__(*args, **values)
        self.collection_name = 'image_test'

    def save_image(self, video_name, image_name, data):
        priority = self.count_by_query({'video_name': video_name})
        if not priority:
            priority = 0
        data_image = {
            "video_name": video_name,
            "image_name": image_name,
            "data": data,
            "created_time": datetime.datetime.utcnow(),
            'priority': priority + 1
        }
        try:
            self.insert(data_image)
        except Exception as e:
            print('Image::save_image():insert image error: %s' % str(e))

    def get_images(self, video_name):
        try:
            print('Image::save_image():get image: {}'.format(video_name))
            return self.find({'video_name': video_name})
        except Exception as e:
            print('Image::save_image():insert image error: %s' % str(e))
