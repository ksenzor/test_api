from marshmallow import fields

from schemas.base_schema import BaseSchema


class GeoSchema(BaseSchema):
    lat = fields.String(load_default=None, allow_none=True)
    lng = fields.String(load_default=None, allow_none=True)

class AddressSchema(BaseSchema):
    street = fields.String(load_default=None, allow_none=True)
    suite = fields.String(load_default=None, allow_none=True)
    city = fields.String(load_default=None, allow_none=True)
    zipcode = fields.String(load_default=None, allow_none=True)
    geo = fields.Nested(GeoSchema(), load_default=None, allow_none=True)

class CompanySchema(BaseSchema):
    name = fields.String(load_default=None, allow_none=True)
    catch_phrase = fields.String(data_key='catchPhrase', load_default=None, allow_none=True)
    bs = fields.String(load_default=None, allow_none=True)

class UsersSchema(BaseSchema):
    id = fields.Integer(load_default=None, allow_none=True)
    name = fields.String(load_default=None, allow_none=True)
    username = fields.String(load_default=None, allow_none=True)
    email = fields.String(load_default=None, allow_none=True)
    address = fields.Nested(AddressSchema(), load_default=None, allow_none=True)
    phone = fields.String(load_default=None, allow_none=True)
    website = fields.String(load_default=None, allow_none=True)
    company = fields.Nested(CompanySchema(), load_default=None, allow_none=True)
