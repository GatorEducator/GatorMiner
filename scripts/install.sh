#!/bin/bash
if [ -f "$(eval 'which pip')" ]
then
	pip_version="pip"
elif [ -f "$(eval 'which pip3')" ]
then
	pip_version="pip3"
else
	$(eval "python3 -m pip install --upgrade pip")
	pip_version="pip"
fi

echo $(eval "$pip_version install pipenv -U")
echo $(eval "cd ..")
echo $(eval "pipenv install")
echo $(eval "pipenv run python -m spacy download en_core_web_sm")
echo $(eval "pipenv run python -m spacy download en_core_web_md")
