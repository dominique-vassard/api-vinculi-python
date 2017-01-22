from eve import Eve
from eve_neo4j import Neo4j
from eve_swagger import swagger, add_documentation


app = Eve(data=Neo4j)

app.register_blueprint(swagger)

# required. See http://swagger.io/specification/#infoObject for details.
app.config['SWAGGER_INFO'] = {
    'title': 'test Eve with Swagger',
    'version': '1.0',
    'description': 'an API description',
    'termsOfService': 'my terms of service',
    # 'contact': {
    #     'name': 'dominique',
    #     'url': '---'
    # },
    # 'license': {
    #     'name': 'BSD',
    #     'url': 'mygithub',
    # }
}

# optional. Will use flask.request.host if missing.
# app.config['SWAGGER_HOST'] = 'localhost:8000'

# optional. Add/Update elements in the documentation at run-time without deleting subtrees.
# add_documentation({'paths': {'/status': {'get': {'parameters': [
#     {
#         'in': 'query',
#         'name': 'foobar',
#         'required': False,
#         'description': 'special query parameter',
#         'type': 'string'
#     }]
# }}}})


@app.route('/test_out_eve')
def tets_out_eve():
    return 'Out of Eve test'


app.run(host='0.0.0.0', debug=True)
