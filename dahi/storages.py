from pymongo import MongoClient


class AbstractCollection(object):

    def find(self, pk):
        raise NotImplemented

    def findAll(self, criteria):
        raise NotImplemented

    def insert(self, object):
        raise NotImplemented

    def update(self, criteria, object):
        raise NotImplemented

    def remove(self, criteria):
        raise NotImplemented

    def __getitem__(self, item):
        raise NotImplemented


class Collection(AbstractCollection):
    def __init__(self, coll):
        super(Collection, self).__init__()
        self.coll = coll

    def findOne(self, criteria):
        return self.coll.find_one(criteria)

    def find(self, criteria):
        return self.coll.find(criteria)

    def insert(self, object):
        return self.coll.insert(object)

    def update(self, criteria, object):
        return self.coll.update(criteria, object)

    def remove(self, criteria):
        return self.coll.remove(criteria)


class Mongo(object):
    def __init__(self, mongoUri):
        super(Mongo, self).__init__()
        self.db = MongoClient(mongoUri)

    def __getitem__(self, item):
        return Collection(self.db[item])
