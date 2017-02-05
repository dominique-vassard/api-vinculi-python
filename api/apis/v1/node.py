from flask_restplus import Resource, fields

from apis.v1.blueprint import api
from apis.auth import requires_auth
import core.utils.validation as validation
import core.schemas.node_input as input_schemas
from core.schemas.graph_output import get_graph_output_schema
from core.schemas.node_output import get_node_output_schema
import core.models.node as node_model


node_api_model = api.model('Node', {
    'firstName': fields.String,
    'lastName': fields.String
})


@api.route('/node/<string:uuid>')
@api.doc(params={'uuid': 'A valid node unique id'},
         security='basic_auth')
class Node(Resource):
    @requires_auth
    @api.marshal_with(get_node_output_schema(api),
                      code=200, description='Success')
    @api.doc('get_node')
    def get(self, uuid):
        params = {'uuid': uuid}
        params, errors = input_schemas.NodeSchema().load(params)
        if errors:
            return errors
        return node_model.get_node_by_uuid(**params)


@api.route('/node/label/<string:label>')
@api.doc(params={'label': 'A valid node label.'},
         security='basic_auth')
class NodeByLabel(Resource):
    @requires_auth
    @api.doc('get_nodes_by_label')
    @api.response(200, 'Success', get_graph_output_schema(api))
    @validation.validate(input_schemas.labelSchema())
    def get(self, **params):
        return node_model.get_nodes_by_label(params['label'])
