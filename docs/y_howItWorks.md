# Important Tools used in the Creation of GatorMiner

## Getting Started

Pipenv is used to handle GatorMiner's dependencies. Pipenv is a python specific tool that can be used in the place of a variety of other packaging tools (bundler, composer, npm, cargo, yarn, etc.). Pipenv creates a virtual environment called virtualenv that is useful for separating dependencies. When you install/uninstall different packages, virtualenv add and remove files from the Pipfile. It also creates the Pipfile.lock which helps to determine the versions of the dependencies to be used.

GatorMiner was developed utilizing Streamlit. Streamlit is a python library that enables the user to easily create a visually appealing app.

## Frequency Analysis and Sentiment Analysis

spacy.load from the SpaCy class reads the pipeline's configuration and loads in the data from the documents. SpaCy is a library used to analyze and understand large amounts of data.

Regular Expressions are provided through the re module. Regular Expressions are used to match certain strings in the document data.

Counter from the collections class and the dict subclass counts hashable objects. The total counts are stored in a dictionary as the values in the objects are stored as the keys.  

TfidfVectorizer from the sklearn.feature_extraction.text class is used to convert raw documents to a matrix of TF-IDF features. TF-IDF evaluates how relevant a word is in a document in relation to a variety of documents. This is calculated by multiplying the number of times a word appears in a document with the inverse document frequency.

CountVectorizer from the sklearn.feature_extraction.text class is used to create a vector of term counts from the words in the documents. The differences between TfidfVectorizer and CountVectorizer is TfidfVectorizer returns a float while the CountVectorizer returns integers.

## Document similarity

TfidfVectorizer from the sklearn.feature_extraction.text class is used to convert raw documents to a matrix of TF-IDF features. TF-IDF evaluates how relevant a word is in a document in relation to a variety of documents. This is calculated by multipliying the number of times a word appears in a document with the inverse document frequency.

Numpy.dot is used to find the dot product of two arrays. NumPy is a library that is helpful when analyzing large and complex arrays and matrices. It can also perform mathematical functions on these arrays.

SpaCy is used to compute document similarity. SpaCy is a library used to analyze and understand large amounts of data.

## Summary

Summerize from the gensim.summarization.summarizer class is used to summarize all of the documents uploaded to GatorMiner. It uses the TextRank algorithm. The Gensim library is used for topic modelling, document indexing and similarity retrieval with large collections of data.

## Topic Modeling

Gensim is used to create a dictionary from a list by adding a key to each word. It is also used to create and LDA model. The LDA model tries to determine topics based on the text in the documents. The Gensim library is used for topic modelling, document indexing and similarity retrieval with large collections of data.

The Pandas DataFrame is used to create a two dimensional table like structure with labeled axises.  
