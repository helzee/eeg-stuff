FROM ubuntu:18.04

ENV SRC_DIR=/src
ENV ENV_DIR=/env

RUN apt install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update
RUN apt install python3.11

ADD test $SRC_DIR
ADD GizmoCommander.py $SRC_DIR
ADD gizmoHttpClient.py $SRC_DIR
ADD requirements.txt $ENV_DIR

RUN pip install -r $ENV_DIR/requirements.txt

RUN






