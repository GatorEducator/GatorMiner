import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    classification_report,
)
from . import analyzer as az

# inspired by:
# https://www.dataquest.io/blog/tutorial-text-classification-in-python-using-spacy/
# https://github.com/hundredblocks/concrete_NLP_tutorial/blob/master/NLP_notebook.ipynb


def get_metrics(y_test, y_predicted):
    """Get evaluation metrics of model
    Accuracy:     the percentage of the total predictions
                  the model makes that are completely correct.
    Precision:    the ratio of true positives to
                  true positives plus false positives in our predictions.
    Recall:       the ratio of true positives to
                  true positives plus false negatives in our predictions.
                  true positives / (true positives+false positives)
    """
    precision = precision_score(y_test, y_predicted, pos_label=None, average="weighted")
    # true positives / (true positives + false negatives)
    recall = recall_score(y_test, y_predicted, pos_label=None, average="weighted")
    # harmonic mean of precision and recall
    f1 = f1_score(y_test, y_predicted, pos_label=None, average="weighted")
    # true positives + true negatives/ total
    accuracy = accuracy_score(y_test, y_predicted)
    return accuracy, precision, recall, f1


class predictors(TransformerMixin):
    """custom transformation with space"""

    def transform(self, X, **transform_params):
        # Cleaning Text
        return [clean_text(text) for text in X]

    def fit(self, X, y=None, **fit_params):
        return self

    def get_params(self, deep=True):
        return {}


# Basic function to clean the text
def clean_text(text):
    # Removing spaces and converting text into lowercase
    return text.strip().lower()


###############################################################
# Read & clean data
###############################################################

# csv path
raw = pd.read_csv(sys.argv[1])

raw.columns = ["text", "relevant", "label"]
# Remove numbers, single characters
raw["text"] = az.normalize(raw["text"])
raw.to_csv("clean.csv")

clean = pd.read_csv("clean.csv")
# add column tokens
clean["tokens"] = clean["text"].apply(az.tokenize)

# The feature to analyze
lst_corpus = clean["text"].tolist()
# The label to test against
lst_labels = clean["label"].tolist()


# The feature set to split (lst_corpus),
# The labels to test against (lst_labels)
# the size to use for the test set (test_size)
# bag of words model
X_train, X_test, y_train, y_test = train_test_split(
    lst_corpus, lst_labels, test_size=0.2, random_state=40
)

###############################################################
###############################################################


###############################################################
# Create pipe and model
###############################################################

# default transform
# X_train_counts, count_vectorizer = az.compute_count_vectorize(X_train)
# X_test_counts = count_vectorizer.transform(X_test)
#
# # tfidf bag of words
# X_train_tfidf, tfidf_vectorizer = az.compute_tfidf(list(X_train))
# X_test_tfidf = tfidf_vectorizer.transform(list(X_test))
#
# # logistic regression with cv model
# clf = LogisticRegression(
#     C=30.0,
#     class_weight="balanced",
#     solver="newton-cg",
#     multi_class="multinomial",
#     n_jobs=-1,
#     random_state=40,
# )
#
# # logistic regression for tfidf model
# clf_tfidf = LogisticRegression(
#     C=30.0,
#     class_weight="balanced",
#     solver="newton-cg",
#     multi_class="multinomial",
#     n_jobs=-1,
#     random_state=40,
# )
#
# clf.fit(X_train_counts, y_train)
# clf_tfidf.fit(X_train_tfidf, y_train)
#
#
# evaluate with default:
#
# y_predicted_counts = clf.predict(X_test_counts)
# y_predicted_tfidf = clf_tfidf.predict(X_test_tfidf)
#
#
# inspect accuracy
#
# accuracy, precision, recall, f1 = get_metrics(y_test, y_predicted_counts)
# accuracy_tfidf, precision_tfidf, recall_tfidf, f1_tfidf = get_metrics(
#     y_test, y_predicted_tfidf
# )
#
# print(
#     "accuracy = %.3f, precision = %.3f, recall = %.3f, f1 = %.3f"
#     % (accuracy, precision, recall, f1)
# )
#
# print(
#     "accuracy = %.3f, precision = %.3f, recall = %.3f, f1 = %.3f"
#     % (accuracy_tfidf, precision_tfidf, recall_tfidf, f1_tfidf)
# )


###############################################################
# Custom transformer using spaCy

# generate a bag of words matrix
bow_vector = CountVectorizer(tokenizer=az.tokenize, ngram_range=(1, 1))
# generate a tfidf matrix: a way of normalize BoW
tfidf_vector = TfidfVectorizer(tokenizer=az.tokenize)

# Create a Pipeline and Generate the Model
pipe = Pipeline(
    [
        ("cleaner", predictors()),
        ("vectorizer", bow_vector),
        ("classifier", LogisticRegression()),
    ]
)

# train and test sets splited above
# fit the pipeline components
pipe.fit(X_train, y_train)

###############################################################
###############################################################


###############################################################
# Evaluate
###############################################################
predicted_spacy = pipe.predict(X_test)

# Model Accuracy
print("Logistic Regression Accuracy:", metrics.accuracy_score(y_test, predicted_spacy))
print(
    "Logistic Regression Precision:", metrics.precision_score(y_test, predicted_spacy)
)
print("Logistic Regression Recall:", metrics.recall_score(y_test, predicted_spacy))

# Model accuracy with get_metric
accuracy_spacy, precision_spacy, recall_spacy, f1_spacy = get_metrics(
    y_test, predicted_spacy
)
print(
    "accuracy = %.3f, precision = %.3f, recall = %.3f, f1 = %.3f"
    % (accuracy_spacy, precision_spacy, recall_spacy, f1_spacy)
)


###############################################################
###############################################################
