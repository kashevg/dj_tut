from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client['dj_tut']


class Inspection(object):
    collection = db['inspections']

    def get_list(self):
        items = self.collection.find().sort([('id', 1)]).limit(10)
        return [item for item in items]

    def get_one(self, id):
        return self.collection.find_one({'id': id.upper()})
