from flask import json, request
from flask_restful import Resource

from schemas.api import ChatControllerSchema

from meta.meta import MetaInfo


class ChatController(Resource):
    def get(self):
        arg_schema = ChatControllerSchema()
        try:
            # Validate args
            args = request.args
            err = arg_schema.validate(args)
            if err:
                raise NotImplementedError('invalid arguments')

            # total chats returned, default 10
            limit = args['limit'] if 'limit' in args else 10
            # pinned chats only, default False
            pinned = args['pinned_only'] if 'pinned_only' in args else False

            total_chats = MetaInfo.client.get_dialogs_count()
            chat_list = MetaInfo.client.get_dialogs(limit=int(limit), pinned_only=bool(pinned))

            return {'chats': json.loads(str(chat_list)), 'total': total_chats}, 200
        except Exception as e:
            return str(e.__repr__()), 400
