from marshmallow import Schema, RAISE, fields


class ValidationShoppingSchema(Schema):
    class Meta:
        unknow = RAISE

    category = fields.String(
        required=False, error_messages={"required": "bad parameter"}
    )
