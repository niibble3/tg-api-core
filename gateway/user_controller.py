from flask import json, request
from flask_restful import Resource

from meta.meta import MetaInfo


class GetMe(Resource):
    def get(self):
        try:
            me = MetaInfo.client.get_me()
            return json.loads(str(me)), 200
        except Exception as e:
            return str(e.__repr__()), 400

