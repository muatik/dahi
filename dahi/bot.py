from dahi import nlu
from dahi.knowledgebase import KnowledgeBase
from dahi.nlu import NLU
from dahi.statement import Statement
from dahi.tfidfTable import TfIdfTable


class Bot(object):
    def __init__(self, botID):
        self.id = botID
        self.knowledgeBase = KnowledgeBase(self.id)

    def respond(self, context, statement):
        docs = list(self.knowledgeBase.getAll())
        nlu = NLU(docs)
        try:
            a = nlu.findBestMatches(statement.text, threshold=0.3, amount=4)
            print a[0]
            a = self.knowledgeBase.get(a[0]).statement.text
        except Exception as e:
            print e.message
            a = "sorry, I did not get it."

        return Statement(a)


    def learn(self, doc):
        self.knowledgeBase.insert(doc)
