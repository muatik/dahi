from dahi.nlu import tokenize
import copy


class TfIdfTable(object):
    EMPTY_TERM_DATA = {"tf": {}, "idf": 0}

    def __init__(self, docs=None):
        super(TfIdfTable, self).__init__()
        self.table = {}
        if docs:
            self.generate(docs)

    def generate(self, docs):
        table = {}

        # filling the table with tf values for each term found in docs
        for doc in docs:
            terms = tokenize(doc.statement.text)
            n = len(terms)

            for t in terms:
                tData = table.get(t, copy.deepcopy(TfIdfTable.EMPTY_TERM_DATA))
                w = tData["tf"].get(doc.id, 0)
                tData["tf"][doc.id] = float(w * n + 1) / n
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

    def getTf(self, term, doc=None, docID=None):
        """

        :param term:
        :param doc:
        :param docID:
        :return:
        """
        if doc:
            docID = doc.id
        if not docID:
            raise AttributeError("either document instance or document id "
                                 "must be given")

        return self.getTfs(term).get(docID, None)

    def getTfDocs(self, term):
        """

        :param term:
        :return:
        """
        return self.getTfs(term).keys()

    def getIdf(self, term):
        return self.table.get(
            term, copy.deepcopy(TfIdfTable.EMPTY_TERM_DATA))["idf"]

    def getTfIdfScore(self, term, doc=None, docID=None):
        """

        :param term:
        :param doc:
        :param docID:
        :return:
        """
        tf = self.getTf(term, docID=docID)
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
