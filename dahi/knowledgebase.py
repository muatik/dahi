
class KnowledgeBase(object):
    def __init__(self):
        self.docs = []

    def insert(self, doc):
        self.docs.append(doc)