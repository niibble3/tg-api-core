from flask import json, request
from flask_restful import Resource

from schemas.api import ParticipantControllerGetSchema

from meta.meta import MetaInfo


class ParticipantController(Resource):
    def get(self):
        arg_schema = ParticipantControllerGetSchema()
        try:
            # Validate args
            args = request.args
            err = arg_schema.validate(args)
            if err:
                raise NotImplementedError('invalid arguments')

            participant = args['user'] if 'users' not in args else args['users']

            user_info = MetaInfo.client.get_users(participant)

            return {'participant': json.loads(str(user_info))}, 200
        except Exception as e:
            return str(e.__repr__()), 400
