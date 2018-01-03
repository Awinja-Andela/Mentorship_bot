import os

from flask import Flask
from flask_restful import Api
from config import config

from app.bot.app_bot import MentorBot, MentorsByStack
from app.models import db

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app(config_name):
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(MentorBot, '/bot')
    api.add_resource(MentorsByStack, '/bot/<stack>')
    app.config.from_object(config[config_name])
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


app = create_app(os.getenv('BOT_CONFIG') or 'default')
false = "false"
query_string_1 = {
    "id": "f95e5b23-a33b-4060-9998-a0ac4d29adf2",
    "timestamp": "2017-11-04T09:11:12.13Z",
    "lang": "en",
    "result": {
        "source": "agent",
        "resolvedQuery": "simon bill, 0709887766, php,laravel",
        "action": "@mentor_details",
        "actionIncomplete": false,
        "parameters": {
            "mentor_details": [
                "fname",
                "lname",
                "0709887766",
                "php",
                ",laravel",
                "jojoawinja@andela.com",
                "@bslang",
                "jojo@medium.com",
                "jojo@github.com",
                "jojo@facebook.com",
                "jojo@linkedin.com"

            ],
            "searches": ""
        },
        "contexts": [],
        "metadata": {
            "intentId": "3a91b492-7f1e-4060-b805-f94bbd4640be",
            "webhookUsed": "true",
            "webhookForSlotFillingUsed": "true",
            "webhookResponseTime": 169,
            "intentName": "joan awinja, 0725792909, python, flask"
        },
        "fulfillment": {
            "speech": "",
            "messages": [
                {
                    "type": 0,
                    "speech": ""
                }
            ]
        },
        "score": 0.8600000143051147
    },
    "status": {
        "code": 206,
        "errorType": "partial_content",
        "errorDetails": "Webhook call failed. \
        Error: Webhook response was empty."
    },
    "sessionId": "9c299333-ca59-4605-9c6b-28db4a843ae9"
}

query_string_2 = {
    "id": "ab28c88e-9c28-463b-9102-04dda562da56",
    "timestamp": "2017-11-04T10:53:32.626Z",
    "lang": "en",
    "result": {
        "source": "agent",
        "resolvedQuery": "i want to learn python",
        "action": "@searches",
        "actionIncomplete": false,
        "parameters": {
            "searches": "python"
        },
        "contexts": [],
        "metadata": {
            "intentId": "0330e0d3-407c-4fdb-a2aa-e880659cfe3d",
            "webhookUsed": "true",
            "webhookForSlotFillingUsed": "true",
            "webhookResponseTime": 174,
            "intentName": "search"
        },
        "fulfillment": {
            "speech": "This people are available to mentor you at the moment:",
            "messages": [
                {
                    "type": 0,
                    "platform": "facebook",
                    "speech": "This people are available to mentor you at the moment:"
                },
                {
                    "type": 0,
                    "platform": "facebook",
                    "speech": ""
                },
                {
                    "type": 0,
                    "speech": "This people are available to mentor you at the moment:"
                }
            ]
        },
        "score": 1
    },
    "status": {
        "code": 206,
        "errorType": "partial_content",
        "errorDetails": "Webhook call failed.\
         Error: Webhook response was empty."
    },
    "sessionId": "9c299333-ca59-4605-9c6b-28db4a843ae9"
}