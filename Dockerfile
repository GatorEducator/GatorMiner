FROM python:3.8.8-buster as base

RUN apt update -y && \
      apt upgrade -y

USER root

RUN apt install -y gcc g++ libffi-dev musl-dev libstdc++6 \
    && python -m pip install --no-cache-dir pip setuptools wheel brotlipy spacy pipenv\
    && apt remove gcc g++ libffi-dev musl-dev
RUN mkdir /programs
COPY . /programs/GATORMINER

FROM base as dependencies
RUN cd /programs/GATORMINER
RUN pipenv run rm Pipfile.lock
RUN pipenv install
RUN pipenv run pip install streamlit
RUN pipenv run spacy download en_core_web_md

FROM dependencies as test

CMD ["pipenv", "run", "streamlit", "run", "streamlit_web.py"]
