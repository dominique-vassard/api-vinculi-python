import core.models.node as node_model
import nose.tools


def test_get_node_by_uuid():
    """Get node by uuid
    """
    node = node_model.get_node_by_uuid('person-2')
    exp_res = {'firstName': u'Adam',
               'lastName': u'SMITH',
               'uuid': u'person-2'}
    nose.tools.assert_dict_equal(node, exp_res)


def test_get_nodes_by_label():
    """Get nodes by label
    """
    jgf = node_model.get_nodes_by_label('Person')
    exp_res = {
                  "graph": {
                    "nodes": [
                      {
                        "metadata": {
                          "lastName": "HUME",
                          "internalLink": "http://arsmagica.fr/polyphonies/hume-david-1711-1776",
                          "externalLink": "https://en.wikipedia.org/wiki/David_Hume",
                          "firstName": "David",
                          "uuid": "person-1"
                        },
                        "type": "Person",
                        "id": 86,
                        "label": "David HUME"
                      },
                      {
                        "metadata": {
                          "lastName": "SMITH",
                          "uuid": "person-2",
                          "firstName": "Adam"
                        },
                        "type": "Person",
                        "id": 91,
                        "label": "Adam SMITH"
                      },
                      {
                        "metadata": {
                          "lastName": "KANT",
                          "uuid": "person-3",
                          "firstName": "Immanuel"
                        },
                        "type": "Person",
                        "id": 94,
                        "label": "Immanuel KANT"
                      },
                      {
                        "metadata": {
                          "lastName": "SCHOPENHAUER",
                          "uuid": "person-4",
                          "firstName": "Arthur"
                        },
                        "type": "Person",
                        "id": 101,
                        "label": "Arthur SCHOPENHAUER"
                      },
                      {
                        "metadata": {
                          "lastName": "WITTGENSTEIN",
                          "uuid": "person-5",
                          "firstName": "Ludwig"
                        },
                        "type": "Person",
                        "id": 106,
                        "label": "Ludwig WITTGENSTEIN"
                      },
                      {
                        "metadata": {
                          "lastName": "HUSSERL",
                          "uuid": "person-6",
                          "firstName": "Edmund"
                        },
                        "type": "Person",
                        "id": 111,
                        "label": "Edmund HUSSERL"
                      },
                      {
                        "metadata": {
                          "lastName": "STEIN",
                          "aka": "St. Teresa Benedicta of the Cross",
                          "uuid": "person-7",
                          "firstName": "Edith"
                        },
                        "type": "Person",
                        "id": 118,
                        "label": "Edith STEIN"
                      },
                      {
                        "metadata": {
                          "lastName": "DURKHEIM",
                          "uuid": "person-8",
                          "firstName": "Emile"
                        },
                        "type": "Person",
                        "id": 121,
                        "label": "Emile DURKHEIM"
                      },
                      {
                        "metadata": {
                          "lastName": "MAUSS",
                          "uuid": "person-9",
                          "firstName": "Marcel"
                        },
                        "type": "Person",
                        "id": 128,
                        "label": "Marcel MAUSS"
                      }
                    ],
                    "edges": []
                  }
                }
    nose.tools.assert_dict_equal(jgf, exp_res)
