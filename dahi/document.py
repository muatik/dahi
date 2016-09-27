from bson import ObjectId
from dahi.statement import Statement


class InvalidDocument(Exception):
    pass


class Document(object):
    def __init__(self, docID=None, botSay=None, humanSay=None, onMatch=None):
        super(Document, self).__init__()
        self.botSay = botSay
        self.humanSay = humanSay
        self.id = docID
        self.onMatch = onMatch

    @staticmethod
    def generate(data):
        botSay = None
        humanSay = None

        if data.get("botSay", None):
            botSay = Statement.generate(data["botSay"])

        if data.get("humanSay", None):
            humanSay = Statement.generate(data["humanSay"])

        return Document(
            docID=str(data["_id"]),
            botSay=botSay,
            humanSay=humanSay,
            onMatch=data["onMatch"])

    def __repr__(self):
        return "Document <{}>".format(self.id)

    def toJson(self):
        return {
            "_id": str(self.id),
            "botSay": self.botSay.toJson() if self.botSay else None,
            "humanSay": self.humanSay.toJson() if self.humanSay else None,
            "onMatch": self.onMatch
        }

    def toDB(self):
        return {
            "_id": ObjectId(self.id),  # FIXME: I don't like ObjectId() here
            "botSay": self.botSay.toDB() if self.botSay else None,
            "humanSay": self.humanSay.toDB() if self.humanSay else None,
            "onMatch": self.onMatch
        }
