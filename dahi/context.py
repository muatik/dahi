class Context(object):
    def __init__(self):
        self.userData = {}
        self.logs = []

    def insert(self, statement):
        self.logs.append(statement)
