from gensim import corpora
from analyzer import normalize
import pickle
import gensim

# https://github.com/susanli2016/Machine-Learning-with-Python/blob/master/topic_modeling_Gensim.ipynb
text_data = []
with open('resources/sampleInput/sample_reflection.txt') as f:
    for line in f:
        tokens = normalize(line)
        text_data.append(tokens)

# print(type(text_data))
dictionary = corpora.Dictionary(text_data)
# print(dictionary)
corpus = [dictionary.doc2bow(text) for text in text_data]

pickle.dump(corpus, open('corpus.pkl', 'wb'))
dictionary.save('dictionary.gensim')

NUM_TOPICS = 5
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=15)
ldamodel.save('model5.gensim')

topics = ldamodel.print_topics(num_words=4)
for topic in topics:
    print(topic)
# dictionary = dictionary.doc2bow(text_data)
