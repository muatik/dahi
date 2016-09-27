

class MatchNotFound(Exception):
    def __init__(self, msg="no answer matched", code=400):
        super(MatchNotFound, self).__init__(msg)
        self.msg = msg
        self.code = code

    def __json__(self):
        return {
            "type": self.__class__.__name__,
            "message": self.msg,
            "code": self.code}

    def __str__(self):
        return "{}: code: {}, message: {}".format(
            self.__class__.__name__,
            self.code,
            self.msg)


class NLU(object):

    def __init__(self, matcher):
        super(NLU, self).__init__()
        self.matcher = matcher

    def findBestMatch(self, matches):
        bestMatch = matches[0]
        score = bestMatch[1]
        if score > 0.2:
            return bestMatch

    def findAnswer(self, text, **kwargs):
        matches = self.matcher.match(text)

        if not matches:
            raise MatchNotFound()

        bestMatch = self.findBestMatch(matches)
        if not bestMatch:
            raise MatchNotFound()

        docID = bestMatch[0]
        score = bestMatch[1]
        return docID, score


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

