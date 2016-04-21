from dahi.nlu import tokenize
import copy


class TfIdfTable(object):
    EMPTY_TERM_DATA = {"tf": {}, "idf": 0}

    def __init__(self, docs=None):
        super(TfIdfTable, self).__init__()
        self.table = {}
        if docs:
            self.generate(docs)

    @classmethod
    def parseStatementID(cls, statementID):
        docID, statementID = statementID.split("-")
        return docID, statementID

    @classmethod
    def toStatementID(cls, docID, statementID):
        return "{}-{}".format(docID, statementID)

    def generate(self, docs):
        table = {}

        # filling the table with tf values for each term found in docs
        for doc in docs:
            for i, statement in enumerate(doc.statements):
                terms = tokenize(statement.text)
                n = len(terms)
                statementID = TfIdfTable.toStatementID(doc.id, i)
                for t in terms:
                    tData = table.get(t, copy.deepcopy(
                        TfIdfTable.EMPTY_TERM_DATA))
                    w = tData["tf"].get(statementID, 0)
                    tData["tf"][statementID] = float(w * n + 1) / n
                    table[t] = tData

        # filling the table with idf values for each term found in the table
        for t in table:
            df = len(table[t]["tf"])
            idf = len(docs) / float(1 + df)
            table[t]["idf"] = idf

        self.table = table

    def getTfs(self, term):
        """

        :param term:
        :return:
        """
        return self.table.get(
            term, copy.deepcopy(TfIdfTable.EMPTY_TERM_DATA))["tf"]

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
            term, copy.deepcopy(TfIdfTable.EMPTY_TERM_DATA))["idf"]

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
    # a = [Document(42, "elma armut elma elma", None),
    #      Document(71, "karpuz armut patates", None),
    #      Document(56, "elma uzum limon", None)]
    # tt = TfIdfTable()
    # tt.generate(a)
    # print tt.table
    # print tt.getTfs("karp")
    # print tt.getIdf("karp")
    # print tt.getTfIdfScore("karp", docID=71)
    pass
