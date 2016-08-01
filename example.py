from dahi.bot import Bot
from dahi.context import Context
from dahi.document import Document
from dahi.knowledgebase import KnowledgeBase
from dahi.matchers.tfidfMatcher import TFIDFMatcher
from dahi.statement import Statement
from dahi.storages import Mongo


storage = Mongo("mongodb://localhost")

kb = KnowledgeBase(storage)
kb.truncate()

kb.insert(Document(
    humanSay=Statement("kredi karti nedir"),
    botSay=Statement("kredi karti nedir dedin")))

kb.insert(Document(
    humanSay=Statement("kredi faizi"),
    botSay=Statement("kredi faizi dedin")))

kb.insert(Document(
    humanSay=Statement("kredi karti"),
    botSay=Statement("kredi karti dedin")))

kb.insert(Document(
    docID=None, humanSay=Statement("elma armut"), onMatch=None))

kb.insert(Document(
    docID=None, humanSay=Statement("elma patates"), onMatch=None))

kb.insert(Document(
    docID=None, humanSay=Statement("elma patates uzum karpuz"), onMatch=None))

context = Context()
bot = Bot(knowledgeBase=kb)
print bot.respond(context, Statement("kredi"))
print bot.respond(context, Statement("faiz"))
print bot.respond(context, Statement("nedir"))
print bot.respond(context, Statement("kredi faizi nedir"))
print bot.respond(context, Statement("tamam"))

print "LOGS:"
for i in context.logs:
    print i
