from dahi.knowledgebase import KnowledgeBase
from dahi.statement import Statement


class Bot(object):
    def __init__(self):
        self.knowledgeBase = KnowledgeBase()

    def teach(self, doc):
        self.knowledgeBase.insert(doc)

    def respond(self, context, statement):
        t = statement.text
        if "elma" in t:
            return Statement("ok I got elma.")
        elif "armut" in t:
            return Statement("ok I got armut.")
        elif "uzum" in t:
            return Statement("ok I got uzum.")
        elif "kiraz" in t:
            return Statement("ok I got kiraz")

        return Statement("sorry, I did not get id.")
