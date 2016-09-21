from bson import ObjectId
from pymongo import MongoClient


class AbstractCollection(object):

    def find(self, pk):
        raise NotImplementedError

    def findAll(self, criteria):
        raise NotImplementedError

    def insert(self, object):
        raise NotImplementedError

    def update(self, criteria, object):
        raise NotImplementedError

    def remove(self, criteria):
        raise NotImplementedError

    def count(self, criteria=None):
        raise NotImplementedError

    def __getitem__(self, item):
        raise NotImplementedError


class Collection(AbstractCollection):
    def __init__(self, coll):
        super(Collection, self).__init__()
        self.coll = coll

    @staticmethod
    def prepareCriteria(criteria):
        if criteria and "id" in criteria:
            criteria["_id"] = ObjectId(criteria["id"])
            criteria.pop("id")
        return criteria

    def findOne(self, criteria):
        criteria = Collection.prepareCriteria(criteria)
        return self.coll.find_one(criteria)

    def find(self, criteria=None):
        criteria = Collection.prepareCriteria(criteria)
        return self.coll.find(criteria)

    def insert(self, object):
        return self.coll.insert(object)

    def update(self, criteria, object):
        criteria = Collection.prepareCriteria(criteria)
        return self.coll.update(criteria, object)

    def remove(self, criteria):
        criteria = Collection.prepareCriteria(criteria)
        return self.coll.remove(criteria)

    def count(self, criteria=None):
        return self.coll.find(criteria).count()


class Mongo(object):
    def __init__(self, mongoUri):
        super(Mongo, self).__init__()
        self.db = MongoClient(mongoUri)["dahi"]

    def __getitem__(self, item):
        return Collection(self.db[item])
