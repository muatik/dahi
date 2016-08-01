from dahi.document import InvalidDocument


class Context(object):
    def __init__(self, contextId):
        self.userData = {}
        self.logs = []

    def insert(self, statement):
        self.logs.append(statement)

    def botSays(self, document):
        """
        insert bot's statement into the logs

        :param document: Document instance
        :return:
        """
        assert document.botSay, InvalidDocument("botSay not found in document")
        self.insert(document.botSay)

    def humanSays(self, statement):
        self.insert(statement)
