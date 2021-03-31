# Welcome to GatorMiner!

GatorMiner is an automated text-mining tool written in Python to measure the technical
responsibility of students in computer science courses. It is being used to analyze
students' markdown reflection documents and five questions survey based on
Natural Language Processing in the Department of Computer Science at Allegheny
College.

### Data Retrieving

There are currently two ways to import text data for analysis: through local file system or AWS DynamoDB.

### Local File System

What is a local file system?

- A controlled place where data can be stored and received. In this case, this
  is where GatorMiner keeps data isolated so it can be easily identified.

In GatorMiner, you can type in the path(s) to the directories(s) that hold
reflection markdown documents. You are welcome to try the tool with the sample
documents. You are welcome to try the tool with the sample documents we provided
in the 'resources', for example:

```shell
resources/sample_md_reflections/lab1, resources/sample_md_reflections/lab2, resources/sample_md_reflections/lab3
```

### AWS

Retrieving reflection documents from AWS is a feature integrated with the use
of [GatorGrader](https://github.com/GatorEducator/gatorgrader) where students'
markdown reflection documents are being collected and stored inside the a
pre-configured DynamoDB database. In order to use this feature, you will need
to have some credential tokens (listed below) stored as environment variables:

```bash
export GATOR_ENDPOINT=<Your Endpoint>
export GATOR_API_KEY=<Your API Key>
export AWS_ACCESS_KEY_ID=<Your Access Key ID>
export AWS_SECRET_ACCESS_KEY=<Your Secret Access Key>
```

It is likely that you already have these prepared when using GatorMiner in
conjunction with GatorGrader, since these would already be exported when
setting up the AWS services. You can read more about setting up an AWS service
with GatorGrader [here](https://github.com/enpuyou/script-api-lambda-dynamodb).

Once the documents are successfully imported, you can then navigate through
the select box in the sidebar to view the text analysis:

<img src="resources/images/select_box.png" alt="browser" style="width:100%"/>

### Analysis

### Frequency Analysis

Frequency analysis is the quantification and analysis of word usage in text (how often a word appears within a certain text). Overall, frequency analysis can provide amazing insight into the many aspects of assignments that instructors may not always be able to observe so it can be extremely valuable to make this information available in a user-friendly and intuitive fashion. This can be achieved using GatorMiner frequency analysis.

Within the GatorMiner tool, you have the ability to choose `Frequency Analysis` as an analysis option after the path to the desired reflection documents is submitted.

When the tool runs a frequency analysis, on any number of assignments, it provides 3 different options to choose from:

- Overall
- Student
- Question

When `Overall` is selected, the application will display a vertical bar chart containing a list of the words used with the highest frequency for each given assignment.

When `Student` is selected, a dropdown menu is provided allowing you to pick which student the tool should display frequency data for. As with `Overall`, this data is also displayed as a vertical bar chart and you can display multiple students' data on the same page in order to compare and contrast the types of words that are being used by student.

Finally, when `Question` is selected, the option to pick one or more specific questions appears. The tool then produces and displays a vertical bar chart which contains frequency information for each of the selected questions in the assignment. This is helpful for comparing the ways in which different terms are utilized within different questions in an assignment.

<img src="resources/images/frequency.png" alt="browser" style="width:100%"/>

### Sentiment Analysis

Sentiment analysis (or opinion mining) is the use of natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information. Overall,
this is a technique to determine whether data is positive, negative, or neutral.

Within the GatorMiner tool, you have the ability to choose `Sentiment Analysis` as an analysis option after the path to the desired reflection documents is submitted.

When the tool runs a Sentiment analysis, on any number of assignments, it provides 3 different options to choose from:

- Overall
- Student
- Question

When `Overall` is selected, a scatter plot and a bar chart appear on the screen
displaying the overall sentiment polarity in, for example, assignment-01 given by the users.

When `Student` is selected, it allows the user to choose a specific student to
observe. When chosen it shows the sentiment shown by the chosen user with a mini bar graph and a bigger version of that using a histogram. Inside this feature, you can also change the number of plots per row.

Finally, when `Question` is selected, it allows the user to choose a certain question in the drop down menu. When chosen, it shows the user the sentiment the question was given.

### Document Similarity

Document similarity analyzes documents and compares text to determine frequency of words between documents.

Within the GatorMiner tool, you have the ability to choose `Document similarity` as an analysis option after the path to the desired reflection documents is submitted.

In the `Document Similarity` section, you are able to select the type of similarity analysis `TF-IDF` and `Spacy`.

When `TF-IDF` is selected, the application will display a frequency matrix showing the correlation between documents. It does this buy dividing the frequency of the word by the total number of terms in a document.

When `Spacy` is selected, the application will display a drop down named 'Model name' with two options:

- `en_core_web_sm` which is used to produce a correlation matrix for **SMALLER** files. (10mb)
- `en_core_web_md` which is used to produce a correlation matrix for **LARGER** files. (>10mb)

**Warning exceeding these limits could cause the program to crash.**

### Topic Modeling
