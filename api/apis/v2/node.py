from flask_restplus import Resource, fields
import marshmallow

import core.models.node as node_model
from apis.v2.blueprint import api


node_api_model = api.model('Node', {
    'firstName': fields.String,
    'lastName': fields.String,
    'version': fields.Integer
})


#   Validation
class NodeSchema(marshmallow.Schema):
    uuid = marshmallow.fields.Str()
    firstName = marshmallow.fields.Str()
    version = marshmallow.fields.Int(default=2)


@api.route('/node/<string:uuid>')
@api.doc(params={'uuid': 'A valid node unique id'})
class Node(Resource):
    @api.marshal_with(node_api_model, code=200, description='Success')
    @api.doc('get_node')
    def get(self, uuid):
        params = {'uuid': uuid}
        params, errors = NodeSchema().load(params)
        if errors:
            return errors
        return node_model.get_node_by_uuid(**params)
