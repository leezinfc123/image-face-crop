"""
 Author: Hieund
 Company: MobioVN
 Date created: 02/11/2021
"""
from pymongo import MongoClient, ReadPreference

from configs import Mongo

db_name = Mongo.DB
mongo_client = MongoClient(Mongo.URI, username='root', password='rootpassword')


class BaseModel:
    collection_name = ''

    def insert(self, dictionary):
        db = mongo_client[db_name]
        return db[self.collection_name].insert_one(dictionary)

    def upsert(self, search_option, dictionary):
        db = mongo_client[db_name]

        document = db[self.collection_name].find_one(search_option)
        if document:
            print('__init__::upsert():update:document: %s' % dictionary)
            document.update(dictionary)
            db[self.collection_name].replace_one(filter=search_option, replacement=document, upsert=True)
        else:
            print('__init__::upsert():insert:document: %s' % dictionary)
            db[self.collection_name].insert_one(dictionary)

    def find(self, search_option):
        db = mongo_client[db_name]

        return db.get_collection(self.collection_name, read_preference=ReadPreference.SECONDARY_PREFERRED).find(
            search_option)

    def find_without_id(self, search_option):
        db = mongo_client[db_name]

        return db.get_collection(self.collection_name, read_preference=ReadPreference.SECONDARY_PREFERRED).find(
            search_option, {'_id': 0})

    def delete_many(self, delete_options):
        db = mongo_client[db_name]
        db[self.collection_name].delete_many(delete_options)

    def update_one(self, search_option, dictionary):
        db = mongo_client[db_name]

        document = db[self.collection_name].find_one(search_option)
        if document:
            print('__init__::update_one():update:document: %s' % dictionary)
            document.update(dictionary)
            db[self.collection_name].replace_one(filter=search_option, replacement=document, upsert=False)

    def update_many(self, filter_option, update_option):
        db = mongo_client[db_name]
        db[self.collection_name].update_many(filter_option, update_option)

    def insert_many(self, document):
        db = mongo_client[db_name]
        db[self.collection_name].insert_many(document)

    def find_one(self, search_options):
        db = mongo_client[db_name]
        return db[self.collection_name].find_one(search_options)

    def delete_one(self, delete_options):
        db = mongo_client[db_name]
        db[self.collection_name].delete_one(delete_options)

    def count_by_query(self, count_option):
        db = mongo_client[db_name]
        return db[self.collection_name].count(count_option)
