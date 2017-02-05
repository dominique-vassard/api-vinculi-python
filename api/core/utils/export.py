from neo4j.v1.types import Node, Relationship

export_types = ('JGF')


def export_to(query_result, export_type):
    """Export query result to a given format

    Available format: JGF

    Arguments:
        query_result (neo4j.v1.bolt.BoltStatementResult): A query result
        export_type (str): The desired format

    Returns:
        (str|dict): A formatted result

    Raises:
        (Exception): If format is nopt valid
    """
    if export_type not in export_types:
        msg = 'Unkown export type. [Valid export types: {}Reveiced: {}]'
        msg = msg.format(export_types, export_type)
        raise Exception(msg)

    result = []
    if export_type == 'JGF':
        result = to_jgf(query_result)

    return result


def to_jgf(query_result):
    """Convert query rsult to JGF format (http://jsongraphformat.info/)

    Arguments:
        query_result (neo4j.v1.bolt.BoltStatementResult): A query result

    Returns:
        (dict): A JGF dictionnary froamtted as :
        ::
            {"graph":
                "edges": [],
                "nodes": [
                    {
                        "id": The node id,
                        "type": The node type (label in Neo4j language)
                        "metadata": The node metadata (properties in Neo4j)
                    }
                ]
            }
    """
    jgf = {
        'graph': {
            'nodes': [],
            'edges': []
        }
    }

    for record in query_result:
        if isinstance(record[0], Node):
            jgf['graph']['nodes'].append({
                'id': record[0].id,
                'type': list(record[0].labels)[0],
                'label': get_label(list(record[0].labels)[0],
                                   dict(record[0].items())),
                'metadata': dict(record[0].items())
            })
        else:
            pass

    return jgf


def get_label(obj_type, metadata):
    label = ''
    if obj_type == "Person":
        label = "{} {}".format(metadata['firstName'], metadata['lastName'])
    elif obj_type == "Publication":
        label = metadata['title']
    elif obj_type in ("Year", "Month", "Day"):
        label = metadata['value']
    else:
        label = metadata.get('name', '')

    return label
