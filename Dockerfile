FROM scratch
ADD alpine-minirootfs-3.13.2-x86_64.tar.gz /
COPY . /DOCKERMINER
RUN make /DOCKERMINER
RUN pip install pipenv -U
RUN pipenv run python -m spacy download en_core_web_md
RUN pipenv install
CMD pipenv run streamlit run streamlit_web.py