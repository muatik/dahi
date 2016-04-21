from dahi.document import Document
from bson import ObjectId


class Documents(object):
    def __init__(self, db):
        super(Documents, self).__init__()
        self.db = db
    
    def getAll(self):
        return (Documents.genDoc(i) for i in self.db.find())

    @staticmethod
    def genDoc(data):
        return Document(
            data["_id"],
            data["statements"],
            data["onMatch"])

    def get(self, docID):
        data = self.db.find_one({"_id": docID})
        return Documents.genDoc(data)

    def insert(self, doc):
        self.db.insert(doc.toDB())

    def update(self, doc):
        self.db.update(
            {"_id": ObjectId(doc.id)},
            doc.toDB())

    def remove(self, doc=None, docID=None):
        if doc:
            docID = doc.id
        elif not docID:
            raise AttributeError("neither document itself or its id is given")
        self.db.remove({"_id": docID})
