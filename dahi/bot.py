from dahi.document import Document
from dahi.matchers.tfidfMatcher import TFIDFMatcher
from dahi.nlu import NLU, MatchNotFound
from dahi.statement import Statement


class Bot(object):

    def __init__(self, knowledgeBase):
        self.knowledgeBase = knowledgeBase
        self.matcher = TFIDFMatcher(knowledgeBase)

    def respond(self, context, statement):
        nlu = NLU(self.matcher)

        context.humanSays(statement)

        # try:
        docID, score = nlu.findAnswer(
            statement.text, threshold=0.3, amount=4)
        doc = self.knowledgeBase.get(docID)
        if doc.botSay:
            statement = doc.botSay
        # except MatchNotFound as e:
        #     FIXME: this should not be literal, instead, knowledgeBase can be
        #     used to get this.
            # statement = Statement("sorry, I did not get it.")

        context.botSays(doc)
        return doc

    def learn(self, doc):
        self.knowledgeBase.insert(doc)
