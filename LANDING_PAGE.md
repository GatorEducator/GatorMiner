## Welcome to GatorMiner!
GatorMiner is an automated text-mining tool written in Python to measure the technical
responsibility of students in computer science courses. It is being used to analyze
students' markdown reflection documents and five questions survey based on
Natural Language Processing in the Department of Computer Science at Allegheny
College.

### Data Retrieving

There are currently two ways to import text data for analysis: through local file system or AWS DynamoDB.

#### Local File System
What is a local file system?
  - A controlled place where data can be stored and received. In this case, this
is where GatorMiner keeps data isolated so it can be easily identified.

In GatorMiner, you can type in the path(s) to the directories(s) that hold
reflection markdown documents. You are welcome  to try the tool with the sample
documents. You are welcome to try the tool with the sample documents we provided
in the 'resources', for example:

```shell
resources/sample_md_reflections/lab1, resources/sample_md_reflections/lab2, resources/sample_md_reflections/lab3
```

#### AWS

### Analysis

#### Frequency Analysis

Frequency analysis is the quantification and analysis of word usage in text (how often a word appears within a certain text). Overall, frequency analysis can provide amazing insight into the many aspects of assignments that instructors may not always be able to observe so it can be extremely valuable to make this information available in a user-friendly and intuitive fashion. This can be achieved using GatorMiner frequency analysis.

Within the GatorMiner tool, you have the ability to choose `Frequency Analysis` as an analysis option after the path to the desired reflection documents is submitted.

When the tool runs a frequency analysis, on any number of assignments, it provides 3 different options to choose from:

  - Overall
  - Student
  - Question

When `Overall` is selected, the application will display a vertical bar chart containing a list of the words used with the highest frequency for each given assignment.

When `Student` is selected, a dropdown menu is provided allowing you to pick which student the tool should display frequency data for. As with `Overall`, this data is also displayed as a vertical bar chart and you can display multiple students' data on the same page in order to compare and contrast the types of words that are being used by student.

Finally, when `Question` is selected, the option to pick one or more specific questions appears. The tool then produces and displays a vertical bar chart which contains frequency information for each of the selected questions in the assignment. This is helpful for comparing the ways in which different terms are utilized within different questions in an assignment.

#### Sentiment Analysis

#### Document Similarity

#### Topic Modeling
