from flask_restplus import fields


def get_graph_output_schema(api):
    """Build and return graph's output schema

    Arguments:
        api (Flask API): Flask API

    Returns:
        (Model): A model describing graph's output
    """
    metadata_model = api.model('Metadata', {
        'depends on ': fields.String,
        'node / edge': fields.String,
        'type / label': fields.String
    })

    nodes_model = api.model('Nodes', {
        'id': fields.Integer(required=True,
                             description='The node database id'),
        'label': fields.String(required=True,
                               description="Built from metadata"),
        'type': fields.String(required=True,
                              description="Also knwon as 'Label' in DB"),
        'metadata': fields.Nested(metadata_model, required=True,
                                  description="Object containing metadata")
    })

    edges_model = api.model('Edges', {
        'id': fields.Integer(),
        'label': fields.String(required=True,
                               description="Built from metadata"),
        'type': fields.String(required=True,
                              description="The relationship type"),
        'metadata': fields.Nested(metadata_model, required=True,
                                  description="Object containing metadata")
    })

    graph_model = api.model('Graph', {
        'nodes': fields.List(fields.Nested(nodes_model, required=True,
                                           description="Can be empty")),
        'edges': fields.List(fields.Nested(edges_model, required=True,
                                           description="Can be empty"))
    })

    node_by_label = api.model('NodeByLabel', {
        'graph': fields.Nested(graph_model)
    })

    return node_by_label
