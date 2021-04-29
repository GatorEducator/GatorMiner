# Installation

You can clone the repository by running the following command:
```
git clone git@github.com:Allegheny-Ethical-CS/GatorMiner.git
```

`cd` into the project root folder:
```
cd GatorMiner
```

This program uses [Pipenv](https://github.com/pypa/pipenv) for dependency management:
- If needed, install and upgrade the `pipenv` with `pip`:
```
pip install pipenv -U
```
- To create a default virtual environment and use the program:
```
pipenv install
```

GatorMiner relies on `en_core_web_sm` and/or `en_core_web_md`, English models trained on written web text (blogs, news, comments, et cetera...) that includes vocabulary, vectors, syntax and entities.

To install the pre-trained model, you can run one of the following commands.
```
pipenv run python -m spacy download en_core_web_sm
```
```
pipenv run python -m spacy download en_core_web_md
```
