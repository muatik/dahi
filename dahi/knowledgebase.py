from bson import ObjectId
from dahi import getDB
from dahi.document import Document
from dahi.statement import Statement


class KnowledgeBase(object):

    def __init__(self, storageEngine, id):
        self.id = ObjectId(id)
        self.docs = []
        self.db = storageEngine["docs"]

    def getAll(self):
        return (Document.generate(i) for i in self.db.find({"kbId": self.id}))

    def get(self, docID):
        data = self.db.findOne({"kbId": self.id, "id": docID})
        return Document.generate(data)

    def insert(self, doc):
        record = doc.toDB()
        record["kbId"] = self.id
        self.db.insert(record)

    def update(self, doc):
        record = doc.toDB()
        record["kbId"] = self.id
        self.db.update({"id": doc.id}, record)

    def remove(self, doc=None, docID=None):
        if doc:
            docID = doc.id
        elif not docID:
            raise AttributeError("neither document itself or its id is given")
        self.db.remove({"kbId": self.id, "id": docID})

    def truncate(self):
        self.db.remove({"kbId": self.id})

    def count(self):
        return self.db.count({"kbId": self.id})
