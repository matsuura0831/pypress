FROM python:3.7

ADD docker/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD docker/dev-requirements.txt /dev-requirements.txt
RUN pip install -r /dev-requirements.txt

WORKDIR /workspace