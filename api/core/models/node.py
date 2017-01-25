# Database
from neo4j.v1 import GraphDatabase, basic_auth


# Manage DB connection
uri = "bolt://localhost:7687"
auth_token = basic_auth("neo4j", "njpa_reil123")
driver = GraphDatabase.driver(uri, auth=auth_token)


def get_node_by_uuid(uuid):
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
