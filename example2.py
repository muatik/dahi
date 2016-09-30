from dahi import bots, contexts
from dahi.contexts import ContextNotFoundError
from dahi.document import Document
from dahi.knowledgebase import KnowledgeBase
from dahi.nlu import MatchNotFound
from dahi.statement import Statement
from dahi.storages import Mongo

storage = Mongo("mongodb://localhost/dahi")
contextId = "57960e326bb20030900eb6d4"
bot1Id = "57e9095c102ee808b06f0ae1"
bot2Id = "57e9095c102ee808b06f0ae2"


try:
    context = contexts.Builder(storage).get(contextId)
except ContextNotFoundError:
    context = contexts.Builder(storage).create({})



bot1 = bots.Builder(storage).get(botId=bot1Id)
# bot2 = bots.Builder(storage).get(botId=bot2Id)
#
# bot1 = bots.Builder(storage).create(botId=bot1Id, meta={})
# bot2 = bots.Builder(storage).create(botId=bot2Id, meta={})

# bot1.learn(Document(
#     botSay=Statement("bot 1 elma dedin"),
#     humanSay=Statement("elma")))
try:
    print(bot1.respond(context, Statement(text="elma")).botSay)
except MatchNotFound:
    print("bot 1 match not found")
# print(context)
# try:
#     print(bot2.respond(context, Statement(text="elma")))
# except MatchNotFound:
#     print("bot 2 match not found")

KnowledgeBase(storage, bot1Id).remove(docID="57ee51816bb2003008fcd4c2")
for doc in KnowledgeBase(storage, bot1Id).getAll():
    print(doc)