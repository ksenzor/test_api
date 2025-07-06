from marshmallow import fields

from schemas.base_schema import BaseSchema


class PostsSchema(BaseSchema):
    id = fields.Integer(load_default=None, allow_none=True)
    title = fields.String(load_default=None, allow_none=True)
    body = fields.String(load_default=None, allow_none=True)
    user_id = fields.Integer(data_key='userId', load_default=None, allow_none=True)

class PostsRequestSchema(BaseSchema):
    title = fields.String(load_default=None, allow_none=True)
    body = fields.String(load_default=None, allow_none=True)
    user_id = fields.Integer(data_key='userId', load_default=None, allow_none=True)
