from marshmallow import Schema, fields


class ChatControllerSchema(Schema):
    limit = fields.Int(required=False, default=10)
    pinned_only = fields.Bool(required=False)


class ParticipantControllerGetSchema(Schema):
    user = fields.Str(required=False)
    users = fields.Str(required=False, validate=lambda x: x.split(','))

