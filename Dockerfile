FROM python:3.5.0

COPY . /home/app

EXPOSE 5000

WORKDIR /home/app

RUN pip install -r requirements.txt

CMD python3 /home/app/run.py