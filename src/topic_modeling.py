import src.analyzer as az
import src.markdown as md
import pickle
import gensim

text_data = [
    az.tokenize(
        az.normalize(
            md.read_file("../resources/cs100f2019_lab05_reflections/reflection1.md")
        )
    )
]
print(text_data)

dictionary = gensim.corpora.Dictionary(text_data)
# print(dictionary)
corpus = [dictionary.doc2bow(text) for text in text_data]

pickle.dump(corpus, open("corpus.pkl", "wb"))
dictionary.save("dictionary.gensim")

NUM_TOPICS = 5
ldamodel = gensim.models.ldamodel.LdaModel(
    corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=15
)
ldamodel.save("model5.gensim")

topics = ldamodel.print_topics(num_words=4)
for topic in topics:
    print(topic)
# dictionary = dictionary.doc2bow(text_data)
