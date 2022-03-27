from marshmallow import Schema, fields


class BoardSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)


class NoteSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    content = fields.String(required=True)
    board_id = fields.Integer(required=True)
