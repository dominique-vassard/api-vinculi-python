###### Vinculi API (python version)

API was developped first in PHP.... Then in NodeJS...
Due to needed script operation (and docs and HATEOAS and simplicity and....) It is moving to python

1. A running neo4j
    `docker run -d --name neo4j_eve --env NEO4J_AUTH=none  -p 7474:7474 -p 7687:7687 neo4j:3.1.0`
2. Build eve application image
`docker build -t test_eve:v1 .`
3. Run eve application container
`docker run  --name test_eve -p 5000:5000 --link=neo4j_eve  test_eve:v1`

In case of problem, you can use the holder.py and docker exec the container