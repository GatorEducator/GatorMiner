# Web Interface

GatorMiner is mainly developed on its web interface with [Streamlit](https://streamlit.io/) in order to provide fast text analysis and visualizations.

In order to run the `Streamlit` interface, type and execute the following command in your terminal:

```
pipenv run streamlit run streamlit_web.py
```

You then will see something like this in your terminal window:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://xxx.xxx.x.x:8501
```

The web interface will automatically be opened in your browser:
<img src="resources/images/landing_page.png" alt="browser" style="width:100%"/>

## Data Retrieving

There are currently two ways to import text data for analysis:
through local file system or AWS DynamoDB.

### Local File System

You can type in the path(s) to the directories that hold reflection markdown documents. You are welcome to try the tool with the sample documents we provided in `resources`, for example:

```
resources/sample_md_reflections/lab1, resources/sample_md_reflections/lab2, resources/sample_md_reflections/lab3
```

### AWS

Retrieving reflection documents from AWS is a feature integrated with the use of [GatorGrader](https://github.com/GatorEducator/gatorgrader) where students' markdown reflection documents are being collected and stored inside the a pre-configured DynamoDB database. In order to use this feature, you will need to have some credential tokens (listed below) stored as environment variables:

```Bash
export GATOR_ENDPOINT=<Your Endpoint>
export GATOR_API_KEY=<Your API Key>
export AWS_ACCESS_KEY_ID=<Your Access Key ID>
export AWS_SECRET_ACCESS_KEY=<Your Secret Access Key>
```

It is likely that you already have these prepared when using GatorMiner in conjunction with GatorGrader, since these would already be exported when setting up the AWS services. You can read more about setting up an AWS service with GatorGrader [here](https://github.com/enpuyou/script-api-lambda-dynamodb).

Once the documents are successfully imported, you can then navigate through the select box in the sidebar to view the text analysis:

<img src="resources/images/select_box.png" alt="select box" style="width:100%"/>

##### Reflection Documents

We are using markdown format for the student reflection documents.
Its organized structure allows us to parse and perform text analysis easily.
With that said, there are few requirements for the reflection document before it
could be seamlessly processed and analyzed with GatorMiner. A
[template](resources/reflection_template.md) is provided within the repo. Note
that the headers with the assignment's and student's ID/name are required.
GatorMiner is set in default to take the first header as assignment name and the
second header as student name.

You can also check out the
[sample json report](resources/sample_json_report/report%201.json) to see the
format of json reports GatorMiner gathers from AWS.

### Analysis

<img src="resources/images/frequency.png" alt="frequency" style="width:100%"/>
<img src="resources/images/sentiment.png" alt="sentiment" style="width:100%"/>
<img src="resources/images/similarity.png" alt="similarity" style="width:100%"/>
<img src="resources/images/topic.png" alt="topic" style="width:100%"/>
