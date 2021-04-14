import numpy as np
import re
import nltk
nltk.download('wordnet')
from sklearn.datasets import load_files
nltk.download('stopwords')
import pickle
from nltk.corpus import stopwords

documents = []

from nltk.stem import WordNetLemmatizer

def normalize(input):
    stemmer = WordNetLemmatizer()

    for sen in range(0, len(input)):
        # Remove all the special characters
        document = re.sub(r'\W', ' ', str(input[sen]))

        # remove all single characters
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

        # Remove single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)

        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)

        # Removing prefixed 'b'
        document = re.sub(r'^b\s+', '', document)

        # Converting to Lowercase
        document = document.lower()

        # Lemmatization
        document = document.split()

        document = [stemmer.lemmatize(word) for word in document]
        document = ' '.join(document)

        documents.append(document)
        print("document: " + document)
        return document

def transform(normalized_input):
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
    normalized_input = vectorizer.fit_transform(normalized_input).toarray()

    from sklearn.feature_extraction.text import TfidfTransformer
    tfidfconverter = TfidfTransformer()
    transformed_input = tfidfconverter.fit_transform(normalized_input).toarray()

    return transformed_input

def train():
    movie_data = load_files(r"categories_training_data")
    X, y = movie_data.data, movie_data.target
    print(type(X))

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    from sklearn.ensemble import RandomForestClassifier
    classifier = RandomForestClassifier(n_estimators=1000, random_state=0)
    classifier.fit(X_train, y_train)

    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

    with open('text_classifier', 'wb') as picklefile:
        pickle.dump(classifier,picklefile)

    with open('text_classifier', 'rb') as training_model:
        model = pickle.load(training_model)

    print(confusion_matrix(y_test, y_pred2))
    print(classification_report(y_test, y_pred2))
    print(accuracy_score(y_test, y_pred2))

def predict(input_doc):
    input = normalize(input_doc)
    print("Normalized input in function: " + input)
    transform(input_doc)
    # finish program
    # y_pred = classifier.predict(X_test) # this line actually predicts
    # print(y_pred)
