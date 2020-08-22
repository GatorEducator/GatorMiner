# Text Mining

[![Build Status](https://travis-ci.com/Allegheny-Mozilla-Fellows/textMining.svg?branch=master)](https://travis-ci.com/Allegheny-Mozilla-Fellows/textMining)
[![codecov](https://codecov.io/gh/Allegheny-Mozilla-Fellows/textMining/branch/master/graph/badge.svg)](https://codecov.io/gh/Allegheny-Mozilla-Fellows/textMining)
[![Built with spaCy](https://img.shields.io/badge/built%20with-spaCy-09a3d5.svg)](https://spacy.io)
[![Built with Streamlit](https://img.shields.io/badge/built%20with-Streamlit-09a3d5.svg)](https://www.streamlit.io/)

An automated text-mining tool written in Python to measure the technical
responsibility of students in computer science courses, being used to analyze
students' reflection documents and five questions survey based on Natural language
processing in the Department of Computer Science at Allegheny College.

## Installation

You can clone the repository by running the following command:

```bash
git clone git@github.com:Allegheny-Mozilla-Fellows/textMining.git
```

`cd` into the project root folder

```bash
cd textMining
```

This program uses [Pipenv](https://github.com/pypa/pipenv) for dependency management.

- If needed, install and upgrade the `pipenv` with `pip`:

  ```bash
  pip install pipenv --user
  ```

- To create virtual environment and use the program:

  ```bash
  pipenv install
  ```

textMining relies on `en_core_web_sm` and `en_core_web_md`, English models trained on
written web text (blogs, news, comments), that includes vocabulary, vectors,
syntax and entities.

To install the pre-trained model, you can run this following command:

```bash
pipenv run python -m spacy download en_core_web_sm
pipenv run python -m spacy download en_core_web_md
```

## Web Interface

textMining is mainly developed on its web interface with [Streamlit](https://www.streamlit.io)
in order to provide fast text analysis and visualizations.

In order to run Streamlit, type and run the following command in your terminal.

```bash
pipenv run streamlit run streamlit_web.py
```

You then will see something like this in your terminal window:

```bash
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://xxx.xxx.x.x:8501
```

the web app will be opened in your browser like this:

![browser](resources/images/landing_page.png)

### Data Retreiving

There are currently two ways to import text data for analysis: through local
file system or AWS DynamoDB.

#### Local File System

You can type in the path(s) to the directorie(s) that hold reflection markdown
documents. You are welcome to try the tool with the sample documents we
provided in `resources`.

#### AWS

Retreiving reflection documents from AWS is a feature intergrated with the use
of [GatorGrader](https://github.com/GatorEducator/gatorgrader) where student's
reflection markdown documents are being collected and stored inside the a
pre-configured DynamoDB database. In order to use this feature, you will need
to have some credential tokens stored as environment variables:

```bash
export GATOR_ENDPOINT=<Your Endpoint>
export GATOR_API_KEY=<Your API Key>
export AWS_ACCESS_KEY_ID=<Your Access Key ID>
export AWS_SECRET_ACCESS_KEY=<Your Secret Access Key>
```

It is likely that you already have these ready when using textMining in
conjunction with GatorGrader, since these would already be exported when
setting up the AWS services. You can view more about setting up an AWS services
with GatorGrader [here](https://github.com/enpuyou/script-api-lambda-dynamodb)

Once the documents are successfully imported, you can then navigate through
the select box in the sidebar to view the analysis:

![select box](resources/images/select_box.png)

##### Reflection Documents

We are using markdown for the student reflection documents, due to the fact that
its organized structure allows us to parse and perform analysis easily. With that
said, there are few requirements for the reflection document before it could be
seamlessly processed and analyzed with our tool. A
[template](resources/reflection_template.md) is provided here. Note that the
headers with the assignment's and student's ID/name are required. TextMining is
set default to take the first header as assignment and the second header as student.

You can also check out the
[sample json report](resources/sample_json_report/report%201.json) to see the
format of json reports textMining gathers from AWS.

### Analysis

![frequency](resources/images/frequency.png)
![sentiment](resources/images/sentiment.png)
![similarity](resources/images/similarity.png)
![topic](resources/images/topic.png)

## Contribute

In order to contribute code or documentation to the project, we encourage you to
install the development dependencies with `pipenv` as follows:

```bash
pipenv install --dev --skip-lock
```

If you want to add a new feature, please ensure that it is
accompanied by high coverage test cases and that you do not break any of the
existing test cases or features.

You can follow these steps to make a branch and add a new feature if you are
already a collaborator on the project. First, you should type the following
command, substituting the name of your feature for the word `feature-name`.

```bash
git checkout -b feature-name
git checkout master
git push -u origin feature-name
```

You can also create a fork of the repository and make contributions on your own
fork. You might want to configure an upstream remote repository for your fork of
textMining, so that you can sync changes from the main project back
into your fork. textMining is configured to use `TravisCI` to test and create
builds for every commit and pull requests. You may want to set up `TravisCI` on
your own fork to enable continuous integration for your development process.

You should open a pull request on the GitHub repository for the new branch or
the fork that you have created once you are ready to merge them into the
master branch of the main project. This pull request should describe the changes
that it will make to the project.

We expect your Pull Respect is passing the build. We hope your code is tested
and well documented. You can run the test suites locally as follows:

```bash
pipenv run pytest
```

It might also be helpful for you to run this following command to see the test
coverage and lines that are missing test:

```bash
pipenv run pytest --cov-config pytest.cov --cov --cov-report term-missing
```

Besides, you are also welcome to report issues, including both feature
requests and bug reports. Feedback is greatly appreciated.
