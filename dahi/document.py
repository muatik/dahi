from bson import ObjectId


class Document(object):
    def __init__(self, docID, statements, onMatch):
        super(Document, self).__init__()
        self.statements = statements if statements else []
        self.id = docID
        self.onMatch = onMatch

    def __repr__(self):
        return "Document <{}>".format(self.id)

    def toJSON(self):
        return {
            "_id": str(self.id),
            "statements": [i.toJSON() for i in self.statements],
            "onMatch": self.onMatch
        }

    def toDB(self):
        return {
            "_id": ObjectId(self.id),  # FIXME: I don't like ObjectId() here
            "statements": [i.toDB() for i in self.statements],
            "onMatch": self.onMatch
        }
