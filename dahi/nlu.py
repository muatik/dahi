import math
import operator

from dahi.document import Document


class NLU(object):
    def __init__(self, docs=None):
        super(NLU, self).__init__()
        from dahi.tfidfTable import TfIdfTable
        self.tfIdfTable = TfIdfTable(docs)

    def learn(self, docs):
        self.tfIdfTable.generate(docs)

    def match(self, query):
        scores = {}

        for term in tokenize(query):
            docIDs = self.tfIdfTable.getTfDocs(term)
            for docID in docIDs:
                termScore = self.tfIdfTable.getTfIdfScore(term,docID=docID)
                scores[docID] = scores.get(docID, 0) + termScore

        return sorted(
            scores.items(), key=operator.itemgetter(1), reverse=True)[:5]


    def findAnswer(self, query):
        matches = self.match(query)

        bestMatch = findBestMatch(matches)
        if not bestMatch:
            raise Exception("no answer matched")

        docID = bestMatch[0]
        return docID, bestMatch[1]


def findBestMatch(matches):
    bestMatch =  matches[0]
    score = bestMatch[1]
    if score > 0.3:
        return bestMatch


def tokenize(text):
    return [t[:4] for t in text.split(" ")]

#
# def tf(term, document):
#     terms = tokenize(document)
#     term_frequency = terms.count(term)
#     document_size = len(terms)
#     return float(term_frequency) / document_size
#
#
# def countDocsContains(term, docs):
#     return sum(1 for i in docs if term in i)
#
#
# def idf(term, docs):
#     return math.log(len(docs) / (float(countDocsContains(term, docs))))
#
#
# def sigmoid(x):
#     return 1 / (1 + math.exp(-x))





def findRepresentativeTerm(doc, docs):
    scores = {}
    for term in tokenize(doc):
        scores[term] = scores.get(term, 0) + tf(term, doc) * idf(term, docs)
    return sorted(scores.items(), key=operator.itemgetter(1), reverse=True)[:5]


def findAnswerThroughContext(query, docs):
    prev_doc = docs[1]
    context_term = findRepresentativeTerm(prev_doc)
    query = query + " " + context_term[0][0]
    return findAnswer(query)




