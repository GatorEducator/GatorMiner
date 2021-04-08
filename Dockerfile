# Python 3.8
FROM python:3.9

EXPOSE 8501

# SHELL ["/bin/bash", "--login", "-c"]

LABEL version="0.1.0"

LABEL description="An automated text-mining tool written in Python to measure \
    the technical responsibility of students in computer science courses, being \
    used to analyze students' markdown reflection documents and five questions \
    survey based on Natural Language Processing in the Department of Computer \
    Science at Allegheny College."

LABEL maintainer="Group 5"

# ENV LANG C.UTF-8
# ENV LANGUAGE C.UTF-8
# # ENV LC_ALL C.UTF-8
# RUN groupadd -r student && \
#     useradd -m -r -g student -d /home/student -s /usr/sbin/nologin -c "student User" student && \
#     mkdir -p /home/student/workdir && \
#     chown -R student:student /home/student
# COPY . /home/student/GATORMINER/

COPY . /gatorminer

WORKDIR /gatorminer

RUN set -e && echo "Installing Pipenv..." \
    && pip install pipenv \
    && echo "Installing dependencies..." \
    && pipenv install --dev --skip-lock \
    && echo "Installing SpaCy models..." \
    && pipenv run python -m spacy download en_core_web_sm \
    && pipenv run python -m spacy download en_core_web_md

# USER root

# RUN apt-get -y -qq update
# RUN apt-get install -y make build-essential python3-distutils python3-dev libssl-dev zlib1g-dev \
#     libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
#     libncursesw5-dev xz-utils libffi-dev liblzma-dev python-openssl git curl file
# ENV HOME /home/student
# WORKDIR /home/student/GATORMINER
# VOLUME ["/home/student/GATORMINER"]

# VOLUME = /src/
# RUN curl https://pyenv.run | bash
# ENV PATH="$HOME/.pyenv/bin:${PATH}"
# RUN export PATH="$HOME/.pyenv/bin:${PATH}"
# RUN echo 'alias python="python3.9"' >> ~/.profile
# RUN echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
# RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc
# RUN echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
# RUN /bin/bash -c "source ~/.bashrc"
# RUN /bin/bash -c "source ~/.profile"
# RUN pyenv install 3.9.2
# RUN pyenv global 3.9.2
# RUN pyenv local 3.9.2
# RUN /bin/bash --login
# RUN curl https://bootstrap.pypa.io/get-pip.py -o ~/get-pip.py
# RUN pyenv exec python ~/get-pip.py
# RUN pyenv exec python -m pip install pipenv
# RUN pyenv exec pipenv run python -m pip install Cython wheel setuptools watchdog
# RUN pyenv exec pipenv install --skip-lock --dev
# RUN pyenv exec pipenv run spacy download en_core_web_sm
# USER student
# ENV USER student
# CMD pyenv exec pipenv run streamlit run streamlit_web.py

CMD ["pipenv", "run", "streamlit", "run", "streamlit_web.py"]
