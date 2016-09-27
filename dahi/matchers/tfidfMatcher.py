import math

import operator

from dahi.matchers.abstracts import AbstractMatcher
from dahi.nlu import tokenize
from copy import deepcopy


class Model(object):
    """
    Term-frequency and inverse-document-frequency data model. This facilitates
    storing and querying TF and IDF values.
    """

    """
    every individual term has the following entry in the data dictionary
    """
    TERM_ENTRY = {
        "tf": {},
        "idf": 0
    }

    def __init__(self):
        super(Model, self).__init__()
        self.data = {}

    def empty(self):
        self.data = {}

    def getEntry(self, term):
        """
        returns the term entry of the model.

        :param term: term as a string
        :return: TERM_ENTRY structured data
        """
        return self.data.get(term, deepcopy(Model.TERM_ENTRY))

    def setTF(self, docId, term, frequency):
        """
        sets the term-frequency value of the given document.

        :param docId: document id
        :param term: term as a string
        :param frequency: frequency as an integer value
        :return:
        """
        entry = self.getEntry(term)
        entry["tf"][docId] = frequency
        self.data[term] = entry

    def setIDF(self, term, frequency):
        """
        sets the inverse-document-frequency of the given term

        :param term: term as a string
        :param frequency: integer
        :return:
        """
        entry = self.getEntry(term)
        entry["idf"] = frequency
        self.data[term] = entry

    def getTF(self, docId, term):
        """
        returns the term-frequency of the given document.

        if either the term or docId does not exists in the model, this will
        return 0 (zero).

        :param docId: document id
        :param term: term as a string
        :return: frequency as an integer value
        """
        # @TODO: test with not available docId and term
        entry = self.getEntry(term)
        return entry["tf"].get(docId, 0)

    def getIDF(self, term):
        """
        returns the inverse-document-frequency of the given term.

        if term does not exists in the model, this will return 0.

        :param term: term as a string
        :return: integer
        """
        entry = self.getEntry(term)
        return entry["idf"]

    def getDF(self, term):
        """
        returns the document frequency of the given term.

        document frequency is the count of how many distinct documents the term
        occurs in.

        :param term:
        :return: document frequency as an integer value
        """
        return len(self.data[term]["tf"])

    def getTerms(self):
        """
        returns all the terms found in the model.

        :return: terms list
        """
        return self.data.keys()

    def getDocIds(self, term):
        """
        returns the list of document ids in which the given term exists

        :param term: term as a string
        :return: document ids list
        """
        entry = self.getEntry(term)
        return entry["tf"].keys()

    def getScore(self, docId, term):
        """
        calculates and returns TF-IDF score according to docId and term

        :param docId: document id
        :param term: term as a string
        :return: float
        """
        tf = self.getTF(docId, term)
        idf = self.getIDF(term)
        return tf * idf


class TFIDFMatcher(AbstractMatcher):

    def __init__(self, knowledgeBase):
        super(TFIDFMatcher, self).__init__()
        self.model = self.generateModel(knowledgeBase)

    @classmethod
    def generateModel(cls, knowledgeBase):
        """
        returns a new TF-IDF model populated with the given knowledgeBase.

        :param knowledgeBase: KnowledgeBase instance
        :return: Model instance
        """
        model = Model()
        # filling the table with tf values for each term found in docs
        for doc in knowledgeBase.getAll():
            if not doc.humanSay:
                continue
            statement = doc.humanSay
            terms = tokenize(statement.text)
            n = len(terms)
            for term in terms:
                tf = model.getTF(docId=doc.id, term=term)
                tf = float(tf * n + 1) / n
                model.setTF(
                    docId=doc.id, term=term, frequency=tf)

        # filling the model with idf values for each term found in the model
        for term in model.getTerms():
            df = model.getDF(term)
            idf = math.log(knowledgeBase.count() / float(1 + df))
            if idf <= 0:
                idf = 1
            model.setIDF(term, idf)

        return model

    def getTfIdfScore(self, term, docId):
        """
        returns the TF-IDF score according to term and docId

        :param term:
        :param docId:
        :return:
        """
        tf = self.model.getTF(docId, term)
        if not tf:
            return None
        return tf * float(self.model.getIDF(term))

    def match(self, text, length=5):
        """
        matches given text against the knowledge base.

        the best matching knowledge base documents will be returned in a list.
        This list will be sorted descending by matching score.

        :param text: query text
        :param length: length of matching list to be returned
        :return: list of the best matching knowledge base documents
        """
        docScores = {}

        for term in tokenize(text):
            for docId in self.model.getDocIds(term):
                termScore = self.model.getScore(docId, term)
                docScores[docId] = docScores.get(docId, 0) + termScore

        return sorted(
            docScores.items(),
            key=operator.itemgetter(1),
            reverse=True)[:length]


if __name__ == '__main__':
    # example
    from dahi.document import Document
    from dahi.statement import Statement
    from dahi.knowledgebase import KnowledgeBase
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
    tt = TFIDFMatcher(kb)
    tt.generate(kb)

    print(tt.table)
    print(tt.getTfs("karp"))
    print(tt.getIdf("karp"))
    print(tt.getTfIdfScore("karp", docID=71))
