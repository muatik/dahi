from dahi.knowledgebase import KnowledgeBase
from dahi.nlu import NLU, MatchNotFound
from dahi.statement import Statement


class Bot(object):

    def __init__(self, botID):
        self.id = botID
        self.knowledgeBase = KnowledgeBase(self.id)

    def respond(self, context, statement):
        docs = list(self.knowledgeBase.getAll())
        nlu = NLU(docs)

        try:
            a = nlu.findAnswer(statement.text, threshold=0.3, amount=4)
            a = self.knowledgeBase.get(a[0]).statement.text
        except MatchNotFound as e:
            # FIXME: this should not be literal, instead, knowledgeBase can be
            # used to get this.
            a = "sorry, I did not get it."

        return Statement(a)

    def learn(self, doc):
        self.knowledgeBase.insert(doc)
