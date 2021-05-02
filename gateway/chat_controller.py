from flask import json, request
from flask_restful import Resource

from meta.meta import MetaInfo


class ChatController(Resource):
    def get(self):
        try:
            total_chats = MetaInfo.client.get_dialogs_count()
            chat_list = MetaInfo.client.get_dialogs()

            return {'chats': json.loads(str(chat_list)), 'total': total_chats}, 200
        except Exception as e:
            return str(e.__repr__()), 400
