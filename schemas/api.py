from marshmallow import Schema, fields


class ChatControllerSchema(Schema):
    limit = fields.Int(required=False, default=10)
    pinned_only = fields.Bool(required=False)


class ParticipantControllerGetSchema(Schema):
    user = fields.Str(required=True)
    users = fields.List(fields.Str(), required=False)

