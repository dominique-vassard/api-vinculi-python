# flask-neo4j has an import problem
# should be
# import py2neo.ogm as ogm
# of
# from py2neo.ext import ogm
GRAPH_DATABASE = 'http://neo4j_eve:7474/db/data/'
GRAPH_USER = 'neo4j'
GRAPH_PASSWORD = 'neo4j'

# TODO: Override this as a default when using Neo4j as a data layer
ITEM_URL = 'regex("[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")'

DOMAIN = {'people': {}}