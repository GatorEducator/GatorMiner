#!/bin/bash
y=$(eval "which pip")

if [ -f "$y" ]
then
	pip_version="pip"
else
	pip_version="pip3"
fi

echo $(eval "$pip_version install pipenv -U")
echo $(eval "pipenv install")
echo $(eval "pipenv run python -m spacy download en_core_web_sm")
echo $(eval "pipenv run python -m spacy download en_core_web_md")
