FROM ubuntu:18.04

WORKDIR /app


RUN apt-get update && \
    apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install -y python3.11
RUN apt-get install -y python3.11-dev
# RUN apt-get install -y python3.11-distutils
# RUN apt-get install -y python3.11-lib2to3
# RUN apt-get install -y python3.11-gdbm
# RUN apt-get install -y python3.11-tk

COPY . .

RUN pip3 install -r requirements.txt

ENV EEG_PORT=26783
ENV GIZMO_PORT=26784

EXPOSE ${EEG_PORT}
EXPOSE ${GIZMO_PORT}

CMD ["python", "-ep", ${EEG_PORT}, "-gp", ${GIZMO_PORT} ]

# `python#.#-dev`: includes development headers for building C extensions
# - `python#.#-venv`: provides the standard library `venv` module
# - `python#.#-distutils`: provides the standard library `distutils` module
# - `python#.#-lib2to3`: provides the `2to3-#.#` utility as well as the standard library `lib2to3` module
# - `python#.#-gdbm`: provides the standard library `dbm.gnu` module
# - `python#.#-tk`: provides the standard library `tkinter` module





