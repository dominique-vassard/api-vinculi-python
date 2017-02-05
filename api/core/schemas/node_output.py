from flask_restplus import fields


def get_node_output_schema(api):
    """Build and return node's output schema

    Arguments:
        api (Flask API): Flask API

    Returns:
        (Model): A model describing node's output
    """
    node_api_model = api.model('Node', {
        'firstName': fields.String,
        'lastName': fields.String
    })

    return node_api_model
