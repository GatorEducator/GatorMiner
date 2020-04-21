from . import analyzer as az
import pickle
import gensim
from typing import List, Tuple


def topic_model(input, NUM_TOPICS=5, NUM_WORDS=4) -> List[Tuple[int, str]]:
    """Find topics from inout text"""
    text_data = [az.tokenize(az.normalize(input))]
    # Create Dictionary by giving id to each word
    id2word = gensim.corpora.Dictionary(text_data)

    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in text_data]

    # Build LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(
        corpus, num_topics=NUM_TOPICS, id2word=id2word, passes=15
    )

    # pickle.dump(corpus, open("corpus.pkl", "wb"))
    # id2word.save("dictionary.gensim")
    # ldamodel.save("model5.gensim")

    topics = ldamodel.print_topics(num_words=NUM_WORDS)

    return topics
