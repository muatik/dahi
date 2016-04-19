class Statement(object):
    def __init__(self, text):
        super(Statement, self).__init__()
        self.text = text

    def toJSON(self):
        return {"text": self.text}

    def toDB(self):
        return self.toJSON()

    def __str__(self):
        return "Statement <\"{}\">".format(self.text)

