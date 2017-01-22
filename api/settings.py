# flask-neo4j has an import problem
# should be
# import py2neo.ogm as ogm
# of
# from py2neo.ext import ogm
GRAPH_DATABASE = 'http://localhost:7474/db/data/'
GRAPH_USER = 'neo4j'
GRAPH_PASSWORD = 'njpa_reil123'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Swagger conf
X_DOMAINS = ['http://localhost:5000',  # The domain where Swagger UI is running
             'http://editor.swagger.io',
             'http://petstore.swagger.io']
X_HEADERS = ['Content-Type', 'If-Match']  # Needed for the "Try it out" buttons

# TODO: Override this as a default when using Neo4j as a data layer
ITEM_URL = 'regex("[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")'

user_schema = {
    'firstName': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15
    },
    'lastName': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 30,
    },
    'login': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 12,
        'required': True,
        # 'unique': True
    }
}
user = {
    'schema': user_schema,
    'resource_methods': ['GET', 'POST', 'DELETE'],

    'datasource': {
        'projection': {
            'login': 0
        }
    },
    'additional_lookup': {
        'url': 'regex("[\w+]")',
        'field': 'login'
    }
}

DOMAIN = {
    'user': user
}

# [{"login": "user1", "firstName": "John", "lastName": "DUFF"}, {"login": "user2"}, {"login": "user3", "firstName": "Richard", "lastName": "DASSAULT"}]