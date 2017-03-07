FROM python:alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app
RUN pip install -r requirements.txt

ADD . /usr/src/app

CMD [ "/usr/src/app/main.py" ]
