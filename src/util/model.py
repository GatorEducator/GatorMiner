import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from . import analyzer as az

# csv path
raw = pd.read_csv(sys.argv[1])

raw.columns = ['text', 'relevant', 'label']
# Remove numbers, single characters
raw['text'] = az.normalize(raw['text'])
raw.to_csv("clean.csv")

clean = pd.read_csv("clean.csv")
# add column tokens
clean["tokens"] = clean["text"].apply(az.tokenize)

lst_corpus = clean["text"].tolist()
lst_labels = clean["label"].tolist()

X_train, X_test, y_train, y_test = train_test_split(
        lst_corpus,
        lst_labels,
        test_size=0.2,
        random_state=40
        )
