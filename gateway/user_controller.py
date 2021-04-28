from flask import json, request
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


class UserMessages(Resource):
    def post(self):
        """
Send message to someone
---
parameters:
  - in: body
    name: body
    description: JSON parameters.
    required: true
    schema:
      id: Message
      properties:
        to:
          type: string
          description: Username.
          example: telegram
        text:
          type: string
          description: Message text.
          example: Hello World!
responses:
  201:
    description: Sended data
    schema:
      id: MessageSend
      properties:
        message:
          type: string
          description: Text sended.
          example: Hello World!
        info:
          type: object
          description: Sended message information
    id: MessageSend
  400:
    description: Error sending message
        """
        try:
            # Get message JSON
            content = request.get_json(force=True)

            # Parse JSON
            send_to = content['to']
            message = content['text']

            # Send user message
            message_info = MetaInfo.client.send_message(f"{send_to}", f"{message}")

            return {'message': message, 'info': json.loads(str(message_info))}, 201
        except Exception as e:
            return str(e.__repr__()), 400
