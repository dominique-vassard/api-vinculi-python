from flask_restplus import Resource, fields
import marshmallow

from apis.auth import requires_auth
import core.models.node as node_model
from apis.v1.blueprint import api


node_api_model = api.model('Node', {
    'firstName': fields.String,
    'lastName': fields.String
})


#   Validation
class NodeSchema(marshmallow.Schema):
    uuid = marshmallow.fields.Str()
    firstName = marshmallow.fields.Str()


authorizations = {
    'basic_auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}


@api.route('/node/<string:uuid>')
@api.doc(params={'uuid': 'A valid node unique id'},
         security='basic_auth')
class Node(Resource):
    @requires_auth
    @api.marshal_with(node_api_model, code=200, description='Success')
    @api.doc('get_node')
    def get(self, uuid):
        params = {'uuid': uuid}
        params, errors = NodeSchema().load(params)
        if errors:
            return errors
        return node_model.get_node_by_uuid(**params)
