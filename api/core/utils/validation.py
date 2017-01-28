from functools import wraps
from flask import abort


def validate(schema):
    """[Decorator] Validate input parameters with the given schema


    Arguments:
        schema (marshmallow schema): The schema to use for validation

    Returns:
        func with valiadted params
        or
        deatiled error
    """
    def decorated(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print kwargs
            params, errors = schema.load(kwargs)
            if errors:
                return {
                    "error": {
                        "code": 1,
                        "message": "invalid input parameters",
                        "details": errors
                    }
                }
            else:
                return func(*args, **params)
        return inner
    return decorated
