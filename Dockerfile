FROM python:3.5.0

COPY . /home/app

EXPOSE 5000

WORKDIR /home/app

# flask-neo4j 0.5.1 has an import problem (py2neo.ogm), then force update to specific commit
RUN pip install -r requirements.txt
RUN pip install --upgrade git+https://github.com/lashex/flask-neo4j.git@c17e22d

CMD python3.5 /home/app/run.py
# CMD python3.5 /home/app/holder.py