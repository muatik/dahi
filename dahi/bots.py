from dahi.bot import Bot
from dahi.knowledgebase import KnowledgeBase


class BotNotFoundError(Exception):
    def __init__(self):
        super(BotNotFoundError, self).__init__()


class Builder(object):
    def __init__(self, storage):
        super(Builder, self).__init__()
        self.storage = storage
        self.collection = storage["bots"]

    def get(self, botId):
        botRecord = self.collection.find({"id": botId})
        if not botRecord:
            raise BotNotFoundError()

        knowledgeBase = KnowledgeBase(self.storage, botId)
        bot = Bot(knowledgeBase)
        return bot

    def create(self, meta):
        botRecord = self.collection.insert({"meta": meta})
        if botRecord:
            return self.get(botRecord)
