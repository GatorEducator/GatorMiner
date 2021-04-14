# Python Version 3.9
FROM python:3.9

LABEL version="0.1.0"

LABEL description="An automated text-mining tool written in Python to measure \
    the technical responsibility of students in computer science courses, being \
    used to analyze students' markdown reflection documents and five questions \
    survey based on Natural Language Processing in the Department of Computer \
    Science at Allegheny College."

LABEL maintainer="Bennett Westfall, Andre Hance, Thomas Antle, Bailey Mastrascia"

COPY . /gatorminer

WORKDIR /gatorminer

RUN set -e && echo "Installing Pipenv..." \
    && pip install pipenv \
    && echo "Installing dependencies..." \
    && pipenv install --dev --skip-lock \
    && echo "Installing SpaCy models..." \
    && pipenv run python -m spacy download en_core_web_sm \
    && pipenv run python -m spacy download en_core_web_md

CMD ["pipenv", "run", "streamlit", "run", "streamlit_web.py"]

EXPOSE 8501
