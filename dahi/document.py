from bson import ObjectId


class Document(object):
    def __init__(self, docID, statement, onMatch):
        super(Document, self).__init__()
        self.statement = statement
        self.id = docID
        self.onMatch = onMatch

    def __repr__(self):
        return "Doc <{}, {}>".format(self.id, self.statement)

    def toJSON(self):
        return {
            "_id": str(self.id),
            "statement": self.statement,
            "onMatch": self.onMatch
        }

    def toDB(self):
        return {
            "_id": ObjectId(self.id),  # FIXME: I don't like ObjectId() here
            "statement": self.statement,
            "onMatch": self.onMatch
        }
