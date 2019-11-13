from gensim.test.utils import datapath
from gensim import utils
import gensim.models


def __iter__(self):
    corpus_path = datapath('cs100f2019_lab05_reflections/reflection22.txt')
    for line in open(corpus_path):
        # assume there's one document per line, tokens separated by whitespace
        yield utils.simple_preprocess(line)


sentences = MyCorpus()
model = gensim.models.Word2Vec(sentences=sentences)

# Main part of model is model.wv, where “wv” stands for “word vectors”.
# We feed the model words it's familiar with, i.e.
vec_king = model.wv['technology']

for i, word in enumerate(model.wv.vocab):
    if i == 10:
        break
    print(word)
