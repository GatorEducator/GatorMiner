# Document Similarity

# What is it?

Document similarity analyzes documents and compares text to determine frequency of words between documents.

Within the GatorMiner tool, you have the ability to choose `Document Similarity` as an analysis option after the path to the desired reflection documents is submitted.

# How to use it?

In the `Document Similarity` section, you are able to select the type of similarity analysis `TF-IDF` and `Spacy`.

When `TF-IDF` is selected, the application will display a frequency matrix showing the correlation between documents. It does this by dividing the frequency of the word by the total number of terms in a document.

When `Spacy` is selected, the application will display a drop down named 'Model name' with two options:

- `en_core_web_sm` which is used to produce a correlation matrix for **SMALLER** files. (<13mb)
- `en_core_web_md` which is used to produce a correlation matrix for **LARGER** files. (>13mb)

**Warning exceeding these file limits could cause the program to crash.**

**See [Spacy.io](https://spacy.io/models/en) for more details of file limits.**
