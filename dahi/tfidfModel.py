from dahi.nlu import tokenize
from copy import deepcopy


class TfIdfModel(object):
    EMPTY_TERM_ITEM = {
        "tf": {},
        "idf": 0
    }

    def __init__(self, knowledgeBase):
        super(TfIdfModel, self).__init__()
        self.table = {}
        self.generate(knowledgeBase)

    @classmethod
    def parseStatementID(cls, statementID):
        docID, statementID = statementID.split("-")
        return docID, statementID

    @classmethod
    def toStatementID(cls, docID, statementID):
        return "{}-{}".format(docID, statementID)

    def generate(self, knowledge_base):
        table = {}

        # filling the table with tf values for each term found in docs
        for doc in knowledge_base.getAll():
            for i, statement in enumerate([doc.humanSay]):
                terms = tokenize(statement.text)
                n = len(terms)
                statementID = TfIdfModel.toStatementID(doc.id, i)
                for t in terms:
                    tData = table.get(t, deepcopy(TfIdfModel.EMPTY_TERM_ITEM))
                    w = tData["tf"].get(statementID, 0)
                    tData["tf"][statementID] = float(w * n + 1) / n
                    table[t] = tData

        # filling the table with idf values for each term found in the table
        for t in table:
            df = len(table[t]["tf"])
            idf = knowledge_base.count() / float(1 + df)
            table[t]["idf"] = idf

        self.table = table

    def getTfs(self, term):
        """

        :param term:
        :return:
        """
        return self.table.get(
            term, deepcopy(TfIdfModel.EMPTY_TERM_ITEM))["tf"]

    def getTf(self, term, statementID):
        """

        :param term:
        :param statementID:
        :return:
        """
        return self.getTfs(term).get(statementID, None)

    def getTfDocs(self, term):
        """

        :param term:
        :return:
        """
        return self.getTfs(term).keys()

    def getIdf(self, term):
        return self.table.get(
            term, deepcopy(TfIdfModel.EMPTY_TERM_ITEM))["idf"]

    def getTfIdfScore(self, term, statementID):
        """

        :param term:
        :param statementID:
        :return:
        """
        tf = self.getTf(term, statementID)
        if not tf:
            return None
        return tf * float(self.getIdf(term))

if __name__ == '__main__':
    # example
    from document import Document
    from statement import Statement
    from knowledgebase import KnowledgeBase
    a = [Document(42, [Statement("elma armut elma elma")], None),
         Document(71, [Statement("karpuz armut patates")], None),
         Document(56, [Statement("elma uzum limon")], None)]

    def getCount():
        return 3

    def getAll():
        return a

    kb = KnowledgeBase(3)
    kb.getAll = getAll
    kb.count = getCount
    tt = TfIdfModel(kb)
    tt.generate(kb)

    print tt.table
    print tt.getTfs("karp")
    print tt.getIdf("karp")
    print tt.getTfIdfScore("karp", docID=71)
    pass
