import marshmallow


class NodeSchema(marshmallow.Schema):
    """Node Schema used for parameters validation

    Extends:
        marshmallow.Schema

    Variables:
        uuid (str): A valid uuid
        firstName (str): A valid firstName
    """
    uuid = marshmallow.fields.Str()
    firstName = marshmallow.fields.Str()


class labelSchema(marshmallow.Schema):
    """Label Schema used for parameters validation

    Extends:
        marshmallow.Schema

    Variables:
        label (str): A valid node label
    """
    label = marshmallow.fields.Str()

    @marshmallow.validates('label')
    def validate_label(self, value):
        if value not in ('Person', 'Year'):
            raise marshmallow.ValidationError('Invalid label.')
