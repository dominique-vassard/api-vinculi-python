from flask import Flask, jsonify
from flask_restplus import Resource, Api, fields

# Database
from neo4j.v1 import GraphDatabase, basic_auth

# Validation
import marshmallow


app = Flask(__name__)
api = Api(app)

# Manage DB connection
uri = "bolt://localhost:7687"
auth_token = basic_auth("neo4j", "njpa_reil123")
driver = GraphDatabase.driver(uri, auth=auth_token)


# Test route
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


# Complete test
#   Validation
class NodeSchema(marshmallow.Schema):
    uuid = marshmallow.fields.Str()
    firstName = marshmallow.fields.Str()

# Marshalling
node_model = api.model('Node', {
    'firstName': fields.String,
    'lastName': fields.String
})


@api.route('/node/<string:uuid>')
class Node(Resource):
    @api.marshal_with(node_model)
    def get(self, uuid):
        params = {'uuid': uuid}
        params, errors = NodeSchema().load(params);
        if errors:
            return errors
        result = []
        with driver.session() as session:
            with session.begin_transaction() as tx:
                query = '''
                        MATCH(n) WHERE n.uuid = {uuid}
                        RETURN n.uuid AS uuid,
                               n.firstName as firstName,
                               n.lastName AS lastName
                        '''
                params = {'uuid': uuid}
                for record in tx.run(query, params):
                    result = {
                        'uuid': record['uuid'],
                        'firstName': record['firstName'],
                        'lastName': record['lastName'],
                    }
        return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
