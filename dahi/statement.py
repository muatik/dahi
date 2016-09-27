class Statement(object):
    """
    Statement is a text message container for both humans and bots.
    """

    def __init__(self, text):
        super(Statement, self).__init__()
        self.text = text

    def toJson(self):
        """

        returns instance's json representation

        :return: JSON
        """
        return {"text": self.text}

    def toDB(self):
        """
        returns instance's suitable representation for database. It actually
        converts all data into python's primitive data types.

        :return: dictionary
        """
        return self.toJson()

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

