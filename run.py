from eve import Eve
from eve_neo4j import Neo4j


app = Eve(data=Neo4j)
app.run(host='0.0.0.0', debug=True)
