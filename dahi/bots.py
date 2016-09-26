from bson import ObjectId

from dahi.bot import Bot
from dahi.knowledgebase import KnowledgeBase


class BotNotFoundError(Exception):
    def __init__(self, message):
        super(BotNotFoundError, self).__init__()
        self.message = message


class Builder(object):
    def __init__(self, storage):
        super(Builder, self).__init__()
        self.storage = storage
        self.collection = storage["bots"]

    def get(self, botId):
        botRecord = self.collection.findOne({"id": botId})
        if not botRecord:
            raise BotNotFoundError("bot {} cannot be found".format(botId))

        knowledgeBase = KnowledgeBase(self.storage, botId)
        bot = Bot(knowledgeBase)
        return bot

    def create(self, botId=None, meta=None):
        if not meta:
            meta = {}

        if botId:
            botRecord = self.collection.insert({
                "_id": ObjectId(botId), "meta": meta})
        else:
            botRecord = self.collection.insert({"meta": meta})

        if botRecord:
            return self.get(botRecord)
