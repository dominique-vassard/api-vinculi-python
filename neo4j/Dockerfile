FROM neo4j:3.1.0
MAINTAINER <Dominique Vassard "dominique.vassard@gmail.com">

ENV APOC_JAR apoc-3.1.0.3-all.jar
ENV APOC_URI https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases/download/3.1.0.3/apoc-3.1.0.3-all.jar

# Add APOC procedures plugin
RUN curl  --location --remote-name ${APOC_URI} \
    && mv ${APOC_JAR} /var/lib/neo4j/plugins/

# Define volumes for data
VOLUME /data
# Import file
VOLUME /var/lib/neo4j/import
# Logs
VOLUME /logs
# Conf files
VOLUME /var/lib/neo4j/conf

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["neo4j"]