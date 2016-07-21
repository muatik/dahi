from dahi.bot import Bot
from dahi.document import Document
from dahi.knowledgebase import KnowledgeBase
from dahi.statement import Statement
from dahi.storages import Mongo

storage = Mongo("mongodb://localhost")

kb = KnowledgeBase(storage)
kb.truncate()

kb.insert(Document(
    docID=None, humanSay=Statement("elma armut"), onMatch=None))

kb.insert(Document(
    docID=None, humanSay=Statement("elma patates"), onMatch=None))

kb.insert(Document(
    docID=None, humanSay=Statement("elma patates uzum karpuz"), onMatch=None))

bot = Bot(knowledgeBase=kb)
bot.respond(None, "elma")