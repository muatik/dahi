class Statement(object):
    def __init__(self, text):
        super(Statement, self).__init__()
        self.text = text

    def toJSON(self):
        """
        returns instance's json representation

        :return: JSON
        """
        return {"text": self.text}

    def toDB(self):
        return self.toJSON()

    def __str__(self):
        return "Statement <\"{}\">".format(self.text)

    @staticmethod
    def generate(data):
        """
        instantiate a statement object populated via data

        :param data: json
        :return: Statement
        """
        return Statement(data["text"])

