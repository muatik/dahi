from bson import ObjectId
from dahi.bot import Bot
from dahi.context import Context
from dahi.document import Document
from dahi.documents import Documents
from dahi.statement import Statement
from flask import Flask, Blueprint, request, jsonify
from pymongo import MongoClient

# TODO: a config file required for flask app
api = Blueprint("api", __name__, url_prefix="/api/v1")

# TODO: move the db initialization into a separate module
db = MongoClient("mongodb://192.168.33.12")["dahi"]
docs = Documents(db["docs"])
botId = 12


@api.route("/docs/")
def getDocs():
    d = Bot(botId).knowledgeBase.getAll()
    # TODO: improve this jsonify operation, make it less verbose
    a = [i.toJSON() for i in d]
    return jsonify({"docs": a})


@api.route("/docs/", methods=["POST"])
def insertDoc():
    question = request.form["question"]
    answer = request.form["answer"]
    #onMatch = 'return """\n{}\n""" '.format(answer)
    onMatch = answer

    doc = Document(ObjectId(), statement=Statement(question), onMatch=onMatch)
    bot = Bot(botId)
    bot.learn(doc)

    # TODO: every response must be in a standard format. restfulApi doc needed.
    return jsonify(doc.toJSON())


@api.route("/answer")
def getAnswer():
    queryStatement = Statement(request.args["q"])

    userId = 3

    bot = Bot(botId)

    context = Context()
    responseStatement = bot.respond(context, queryStatement)

    context.insert(queryStatement)
    context.insert(responseStatement)
    return jsonify(responseStatement.toJSON())


def run():
    app = Flask(__name__)
    app.register_blueprint(api)
    app.debug = True
    app.run()

if __name__ == "__main__":
    run()
