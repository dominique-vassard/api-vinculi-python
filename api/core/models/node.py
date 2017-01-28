# Database
from neo4j.v1 import GraphDatabase, basic_auth

# Export
import core.utils.export as export


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


def get_nodes_by_label(label):
    """Get first 100  nodes for a given label

    Arguments:
        label (str|unicode): A valid label

    Returns:
        (dict): A JGF formatted dictionnay with the first 100 nodes

    Raises:
        (Exception): If label is invalid (not a str, not a unicode or empty)
    """
    if ((not type(label) == str and not type(label) == unicode) or
       len(label) == 0):
        raise Exception('Invalid label. [Received: {}]'.format(label))

    result = []
    with driver.session() as session:
        with session.begin_transaction() as tx:
            query = 'MATCH (n:{}) RETURN n LIMIT 100'.format(label)
            res = tx.run(query)
            result = export.export_to(res, 'JGF')

    return result
