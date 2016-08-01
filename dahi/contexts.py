from dahi.context import Context


class ContextNotFoundError(Exception):
    def __init__(self):
        super(ContextNotFoundError, self).__init__()


class Builder(object):
    def __init__(self, storage):
        super(Builder, self).__init__()
        self.storage = storage
        self.collection = storage["contexts"]

    def get(self, contextId):
        try:
            contextRecord = self.collection.findOne({"id": contextId})
            if not contextRecord:
                raise ContextNotFoundError()
            return Context(contextId)
        except TypeError:
            raise ContextNotFoundError()

    def create(self, meta):
        contextRecord = self.collection.insert({"meta": meta})
        return self.get(contextRecord)
