from dahi import nlu
from dahi.knowledgebase import KnowledgeBase
from dahi.statement import Statement


class Bot(object):
    def __init__(self, botID):
        self.id = botID
        self.knowledgeBase = KnowledgeBase(self.id)

    def respond(self, context, statement):
        docs = [i.statement.text for i in self.knowledgeBase.getAll()]
        try:
            a = nlu.findAnswer(statement.text, docs)
            a = docs[a[0]]
        except Exception as e:
            a = "sorry, I did not get it."

        return Statement(a)


    def learn(self, doc):
        self.knowledgeBase.insert(doc)
