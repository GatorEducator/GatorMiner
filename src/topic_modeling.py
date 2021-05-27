"""Topic modeling"""
from typing import List, Tuple

import gensim
import pandas as pd
import numpy as np

from sklearn.manifold import TSNE

# import pickle


# pylint: disable=unused-argument
def topic_model(tokens, num_topics=5, num_words=4) -> List[Tuple[int, str]]:
    """Find topics from inout text"""
    # Create Dictionary by giving id to each word
    id2word = gensim.corpora.Dictionary(tokens)

    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in tokens]

    # Build LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(
        corpus,
        num_topics=num_topics,
        id2word=id2word,
        random_state=100,
        update_every=1,
        chunksize=10,
        passes=10,
        alpha='symmetric',
        iterations=100,
        per_word_topics=True
    )

    # pickle.dump(corpus, open("corpus.pkl", "wb"))
    # id2word.save("dictionary.gensim")
    # ldamodel.save("model5.gensim")

    # dominant topic and its percentage contribution in each document
    # topics = ldamodel.print_topics(num_words=NUM_WORDS)
    dom_topic_df = format_topics_sentences(ldamodel, corpus, tokens)
    return dom_topic_df, ldamodel, corpus


def format_topics_sentences(ldamodel, corpus, texts):
    """format topic sentences from model to dataframe"""
    # Init output
    sent_topics_df = pd.DataFrame()

    # Get main topic in each document
    for row_list in ldamodel[corpus]:
        row = row_list[0] if ldamodel.per_word_topics else row_list
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        print(row)
        # Get the Dominant topic, Perc Contribution and Keywords for each doc
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # => dominant topic
                word_prop = ldamodel.show_topic(topic_num)
                topic_keywords = ", ".join([word for word, prop in word_prop])
                sent_topics_df = sent_topics_df.append(
                    pd.Series([int(topic_num),
                               round(prop_topic, 4),
                               topic_keywords]),
                    ignore_index=True)
            else:
                break

    sent_topics_df.columns = [
        'Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']
    # Add original text to the end of the output
    contents = pd.Series(texts)
    sent_topics_df["Text"] = contents

    return sent_topics_df


def tsne(lda_model, corpus, overall_topic_df, random_state, angle):
    """Compute tsne and return result in dataframe."""
    topic_weights = []
    for i, row_list in enumerate(lda_model[corpus]):
        topic_weights.append([w for i, w in row_list[0]])

    # Array of topic weights
    arr = pd.DataFrame(topic_weights).fillna(0).values

    # st.write(arr)

    # Keep the well separated points (optional)
    arr = arr[np.amax(arr, axis=1) > 0.35]

    # st.write(arr)

    # Dominant topic number in each doc
    topic_num = np.argmax(arr, axis=1)

    # st.write(topic_num)

    # tSNE Dimension Reduction
    tsne_model = TSNE(
        n_components=2,
        verbose=1,
        random_state=random_state,
        angle=angle / 100,
        init="pca",
    )
    tsne_lda = tsne_model.fit_transform(arr)

    df_tsne = pd.DataFrame(
        {
            "x": tsne_lda[:, 0],
            "y": tsne_lda[:, 1],
            "topic": topic_num,
            "topic_num": overall_topic_df["Dominant_Topic"],
        }
    )
    # df_tsne["topic_num"] = overall_topic_df["Dominant_Topic"]
    # st.write(df_tsne)
    return df_tsne
