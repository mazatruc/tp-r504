FROM debian:11

RUN apt-get update && apt-get -y upgrade && \
    apt-get -y install build-essential pkg-config python-dev python3-pip default-libmysqlclient-dev && \
    pip3 install --upgrade pip && \
    pip3 install flask-mysqldb mysql-connector-python

RUN mkdir -p /srv/templates

COPY ./index.html /srv/templates/index.html
COPY ./app_1.py /srv/app1.py

CMD ["flask", "--app", "/srv/app1", "run", "--host=0.0.0.0"]