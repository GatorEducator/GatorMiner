#This is how you do comments
FROM ubuntu:20.04
LABEL version="0.1"
LABEL description="An automated text-mining tool written in Python to measure \
    the technical responsibility of students in computer science courses, being \
    used to analyze students' markdown reflection documents and five questions \
    survey based on Natural Language Processing in the Department of Computer \
    Science at Allegheny College."
LABEL maintainer="Group 5"

ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8
RUN groupadd -r student && \
    useradd -m -r -g student -d /home/student -s /usr/sbin/nologin -c "student User" student && \
    mkdir -p /home/student/workdir && \
    chown -R student:student /home/student 
COPY . /home/student/GATORMINER/


USER root
RUN apt-get -y -qq update 
RUN apt-get install -y make build-essential python3-distutils libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
    libncursesw5-dev xz-utils libffi-dev liblzma-dev python-openssl git



ENV HOME /home/student
WORKDIR /home/student/GATORMINER
VOLUME ["/home/student/GATORMINER"]
RUN curl https://pyenv.run | bash
ENV PATH="$HOME/.pyenv/bin:${PATH}"
RUN echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc
RUN echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]
RUN pyenv install 3.9.2
RUN pyenv global 3.9.2
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install pipenv
RUN pipenv run python -m pip install Cython wheel setuptools
#==========This is where the issues start===========
RUN pipenv install --dev
#^^^Last Build Time > 1003.9s before crash
RUN pipenv run spacy download en_core_web_sm
USER student
ENV USER student
CMD pipenv run streamlit run streamlit_web.py


#BUILD WITH: docker build -t gatorminerv1.0 Documents/COMPSCI203/Labs/GatorMiner
#RUN WITH: docker container run --name myminer -d -p 8501:8501 gatorminerv0.1 && echo "Please open 'localhost:80' on your browser of choice"


#TODO: 
#break into subprocesses

#figure out why program fails on pipenv install
#add full comments so that docker file is readable
#push v1 of Docker image!!