import abc


class AbstractMatcher(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match(self, text):
        """
        matches given text

        :param text:
        :return:
        """
        raise NotImplementedError