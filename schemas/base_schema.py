from marshmallow import Schema, post_dump


class BaseSchema(Schema):

    @post_dump
    def remove_skip_values(self, data, many):
        return {
            key: value for key, value in data.items()
            if value is not None and value != 'null'
        }
