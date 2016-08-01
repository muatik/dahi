from pymongo import MongoClient


def getDB():
    db = MongoClient("mongodb://localhost")["dahi"]
    return db

CONFIG = {
    "matcher": "dahi.matchers.tfidfMatcher.TFIDFMatcher",
    "nlu": "dahi.nlu.NLU",
}

#
# def import_component(name, config):
#     def load(path):
#         components = path.split('.')
#         mod = __import__(components[0])
#         for comp in components[1:]:
#             mod = getattr(mod, comp)
#         return mod
#
#     path = config[name] if config else CONFIG[name]
#     return load(path)
