from flask import json
from flask_restful import Resource

from meta.meta import MetaInfo


class GetMe(Resource):

    def get(self):
        """
       Get logged user information
       ---
       responses:
         200:
           description: User information
           schema:
             id: UserInfo
             properties:
               id:
                 type: integer
                 description: The id of the user
               first_name:
                 type: string
                 description: The first name of the user
        """
        try:
            me = MetaInfo.client.get_me()
            return json.loads(str(me)), 200
        except Exception as e:
            return str(e.__repr__()), 400

