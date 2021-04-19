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
