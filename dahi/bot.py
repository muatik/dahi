from dahi.knowledgebase import KnowledgeBase
from dahi.nlu import NLU, MatchNotFound
from dahi.statement import Statement


class Bot(object):

    def __init__(self, knowledgeBase):
        self.knowledgeBase = knowledgeBase

    def respond(self, context, statement):
        nlu = NLU(context, self.knowledgeBase)

        try:
            docID, statementID, score = nlu.findAnswer(
                statement.text, threshold=0.3, amount=4)
            a = self.knowledgeBase.get(docID).statements[int(statementID)].text
        except MatchNotFound as e:
            # FIXME: this should not be literal, instead, knowledgeBase can be
            # used to get this.
            a = "sorry, I did not get it."

        return Statement(a)

    def learn(self, doc):
        self.knowledgeBase.insert(doc)
