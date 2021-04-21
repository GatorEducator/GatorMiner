"""Web interface"""

import re

import base64
import numpy as np
import os
import pandas as pd
from sklearn.manifold import TSNE
import spacy
import streamlit as st
from textblob import TextBlob

import src.analyzer as az
import src.constants as cts
import src.doc_similarity as ds
import src.get_handler as gh
import src.json_util as ju
import src.markdown as md
import src.summarizer as sz
import src.topic_modeling as tm
import src.visualization as vis
import src.grammar_analyzer as ga


# resources/sample_reflections/lab1, resources/sample_reflections/lab2

# initialize main_df and preprocessed_Df
SPACY_MODEL_NAMES = ["en_core_web_sm", "en_core_web_md"]
preprocessed_df = pd.DataFrame()
main_df = pd.DataFrame()
assignments = None
assign_text = None
stu_id = None
success_msg = None
debug_mode = False

def main():
    """main streamlit function"""
    # Title
    st.sidebar.title("Welcome to GatorMiner!")
    data_retreive_method = st.sidebar.selectbox(
            "Choose the data retrieving method",
            [
                "Local file system",
                "AWS",
            ],
        )
    if retreive_data(data_retreive_method):
        analysis_mode = st.sidebar.selectbox(
            "Choose the analysis mode",
            [
                "Home",
                "Frequency Analysis",
                "Sentiment Analysis",
                "Document Similarity",
                "Summary",
                "Topic Modeling",
                "Interactive",
                "Grammar Checker"
            ],
        )
        if debug_mode:
            st.write(main_df)
        if analysis_mode == "Home":
            readme()
        else:
            if analysis_mode == "Frequency Analysis":
                st.title(analysis_mode)
                frequency()
            elif analysis_mode == "Sentiment Analysis":
                st.title(analysis_mode)
                sentiment()
            elif analysis_mode == "Document Similarity":
                st.title(analysis_mode)
                doc_sim()
            elif analysis_mode == "Summary":
                st.title(analysis_mode)
                summary()
            elif analysis_mode == "Topic Modeling":
                st.title(analysis_mode)
                tpmodel()
            elif analysis_mode == "Interactive":
                st.title(analysis_mode)
                interactive()
            elif analysis_mode == "Grammar Checker":
                st.title(analysis_mode)
                grammar_analyzer()
            success_msg.empty()

def readme():
    """function to load and configurate readme source"""

    with open("README.md") as readme_file:
        readme_src = readme_file.read()
        for file in os.listdir("resources/images"):
            if file.endswith(".png"):
                img_path = f"resources/images/{file}"
                with open(img_path, "rb") as f:
                    img_bin = base64.b64encode(f.read()).decode()
                readme_src = readme_src.replace(img_path, f"data:image/png;base64,{img_bin}")

        st.markdown(readme_src, unsafe_allow_html=True)

def landing_pg():
    """landing page"""
    landing = st.sidebar.selectbox("Welcome", ["Home", "Interactive"])

    if landing == "Home":
        readme()
    else:
        interactive()


def retreive_data(data_retreive):
    """pipeline to retrieve data from user input to output"""
    global preprocessed_df
    global main_df
    if data_retreive == "Local file system":
        input_assignments = st.sidebar.text_input(
                "Enter path(s) to markdown documents (seperate by comma)"
        )
    else:
        input_assignments = st.sidebar.text_input(
                "Enter assignment names of the markdown \
documents(seperate by comma)"
        )
        st.sidebar.info(
            "You will need to store keys and endpoints in the \
environment variables")
    if not input_assignments:
        landing_pg()
    else:
        input_assignments = re.split(r"[;,\s]\s*", input_assignments)
        try:
            main_df, preprocessed_df = import_data(
                data_retreive, input_assignments)
        except TypeError:
            st.sidebar.warning(
                "No data imported. Please check the reflection document input")
            readme()
        else:
            global success_msg
            success_msg = None
            if main_df.empty is not True:
                success_msg = st.sidebar.success("Sucessfully Loaded!!")
            global assign_id
            assign_id = preprocessed_df.columns[0]
            global assignments
            assignments = st.sidebar.multiselect(
                label="Select assignments below:",
                options=main_df[assign_id].unique(),
            )
            global assign_text
            assign_text = ", ".join(assignments)
            global stu_id
            stu_id = preprocessed_df.columns[1]
            return True


@st.cache(allow_output_mutation=True)
def load_model(name):
    """load spacy model"""
    return spacy.load(name)


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def import_data(data_retreive_method, paths):
    """pipeline to import data from local or aws"""
    json_lst = []
    if data_retreive_method == "Local file system":
        try:
            for path in paths:
                json_lst.append(md.collect_md(path))
        except FileNotFoundError as err:
            st.sidebar.text(err)
            readme()
    else:
        passbuild = st.sidebar.checkbox(
            "Only retreive build success records", value=True)
        try:
            configs = gh.auth_config()
            for path in paths:
                response = gh.get_request(path, passbuild, **configs)
                json_lst.append(ju.clean_report(response))
        except (EnvironmentError, Exception) as err:
            st.sidebar.error(err)
            readme()
    # when data is retreived
    if json_lst:
        raw_df = pd.DataFrame()
        for item in json_lst:
            single_df = pd.DataFrame(item)
            raw_df = pd.concat([raw_df, single_df]).fillna("")
        tidy_df = df_preprocess(raw_df)
        return tidy_df, raw_df


def df_preprocess(df):
    """build and preprocess (combine, normalize, tokenize) text"""
    # filter out first two columns -- non-report content
    cols = df.columns[2:]
    # combining text into combined column
    df["combined"] = df[cols].apply(
        lambda row: "\n".join(row.values.astype(str)), axis=1
    )
    # normalize
    df[cts.NORMAL] = df["combined"].apply(lambda row: az.normalize(row))
    # tokenize
    df[cts.TOKEN] = df[cts.NORMAL].apply(lambda row: az.tokenize(row))
    return df


def frequency():
    """main function for frequency analysis"""
    freq_type = st.sidebar.selectbox(
        "Type of frequency analysis", ["Overall", "Student", "Question"]
    )
    if freq_type == "Overall":
        freq_range = st.sidebar.slider(
            "Select a range of Most frequent words", 1, 50, value=25
        )
        st.sidebar.success(
            'To continue see individual frequency analysis select "Student"'
        )
        st.header(f"Overall most frequent words in **{assign_text}**")
        overall_freq(freq_range)
    elif freq_type == "Student":
        freq_range = st.sidebar.slider(
            "Select a range of Most frequent words", 1, 20, value=10
        )
        st.header(
            f"Most frequent words by individual students in **{assign_text}**"
        )
        student_freq(freq_range)
    elif freq_type == "Question":
        freq_range = st.sidebar.slider(
            "Select a range of Most frequent words", 1, 20, value=10
        )
        st.header(
            f"Most frequent words in individual questions in **{assign_text}**"
        )
        question_freq(freq_range)


def overall_freq(freq_range):
    """page fore overall word frequency"""
    plots_range = st.sidebar.slider(
        "Select the number of plots per row", 1, 5, value=3
    )
    freq_df = pd.DataFrame(columns=["assignments", "word", "freq"])
    # calculate word frequency of each assignments
    for item in assignments:
        # combined text of the whole assignment
        combined_text = " ".join(
            main_df[main_df[assign_id] == item][cts.NORMAL]
        )
        item_df = pd.DataFrame(
            az.word_frequency(combined_text, freq_range),
            columns=["word", "freq"],
        )
        item_df["assignments"] = item
        freq_df = freq_df.append(item_df)
    # plot all the subplots of different assignments
    st.altair_chart(
        vis.facet_freq_barplot(
            freq_df, assignments, "assignments", plots_per_row=plots_range
        )
    )


def student_freq(freq_range):
    """page for individual student's word frequency"""
    students = st.multiselect(
        label="Select specific students below:",
        options=main_df[stu_id].unique(),
    )

    plots_range = st.sidebar.slider(
        "Select the number of plots per row", 1, 5, value=3
    )
    freq_df = pd.DataFrame(columns=["student", "word", "freq"])
    stu_assignment = main_df[
        (main_df[stu_id].isin(students))
        & main_df[assign_id].isin(assignments)
    ]
    if len(students) != 0:
        for student in students:
            for item in assignments:
                individual_freq = az.word_frequency(
                    stu_assignment[
                        (stu_assignment[assign_id] == item)
                        & (stu_assignment[stu_id] == student)
                    ]
                    .loc[:, ["combined"]]
                    .to_string(),
                    freq_range,
                )
                ind_df = pd.DataFrame(individual_freq, columns=["word", "freq"])
                ind_df["assignments"] = item
                ind_df["student"] = student
                freq_df = freq_df.append(ind_df)
        st.altair_chart(
            vis.facet_freq_barplot(
                freq_df,
                students,
                "student",
                color_column="assignments",
                plots_per_row=plots_range,
            )
        )


def question_freq(freq_range):
    """page for individual question's word frequency"""
    # drop columns with all na
    select_preprocess = preprocessed_df[
        preprocessed_df[assign_id].isin(assignments)
    ].dropna(axis=1, how="all")
    questions = st.multiselect(
        label="Select specific questions below:",
        options=select_preprocess.columns[2:],
    )

    plots_range = st.sidebar.slider(
        "Select the number of plots per row", 1, 5, value=1
    )

    freq_question_df = pd.DataFrame(columns=["question", "word", "freq"])

    select_text = {}
    for question in questions:
        select_text[question] = main_df[question].to_string(
            index=False, na_rep=""
        )
    question_df = pd.DataFrame(
        select_text.items(), columns=["question", "text"]
    )
    if len(questions) != 0:
        for question in questions:
            quest_freq = az.word_frequency(
                question_df[question_df["question"] == question]
                .loc[:, ["text"]]
                .to_string(),
                freq_range,
            )
            ind_df = pd.DataFrame(quest_freq, columns=["word", "freq"])
            ind_df["question"] = question
            freq_question_df = freq_question_df.append(ind_df)

        st.altair_chart(
            vis.facet_freq_barplot(
                freq_question_df,
                questions,
                "question",
                plots_per_row=plots_range,
            )
        )


def sentiment():
    """main function for sentiment analysis"""
    senti_df = main_df.copy(deep=True)
    # calculate overall sentiment from the combined text
    senti_df[cts.SENTI] = senti_df["combined"].apply(
        lambda x: TextBlob(az.lemmatized_text(x)).sentiment.polarity
    )
    senti_df = senti_df[senti_df[assign_id].isin(assignments)]
    senti_type = st.sidebar.selectbox(
        "Type of sentiment analysis", ["Overall", "Student", "Question"]
    )
    if senti_type == "Overall":
        st.sidebar.success(
            'To continue see individual sentiment analysis select "Student"'
        )
        st.header(f"Overall sentiment polarity in **{assign_text}**")
        overall_senti(senti_df)
    elif senti_type == "Student":
        st.header(f"View sentiment by individual students in **{assign_text}**")
        student_senti(senti_df)
    elif senti_type == "Question":
        st.header(
            f"View sentiment by individual questions in **{assign_text}**"
        )
        question_senti(senti_df)


def overall_senti(senti_df):
    """page for overall senti"""
    # display line plot when there are multiple assingments
    if len(assignments) > 1:
        st.altair_chart(vis.stu_senti_lineplot(senti_df, stu_id))
    st.altair_chart((vis.senti_combinedplot(senti_df, stu_id)))


def student_senti(input_df):
    """page for display individual student's sentiment"""
    students = st.multiselect(
        label="Select specific students below:",
        options=input_df[stu_id].unique(),
    )
    plots_range = st.sidebar.slider(
        "Select the number of plots per row", 1, 5, value=3
    )
    df_selected_stu = input_df.loc[input_df[stu_id].isin(students)]
    senti_df = pd.DataFrame(
        df_selected_stu, columns=[assign_id, stu_id, cts.SENTI]
    )
    if len(students) != 0:
        st.altair_chart(
            vis.facet_senti_barplot(
                senti_df, students, stu_id, plots_per_row=plots_range
            )
        )
        st.altair_chart(vis.stu_senti_barplot(senti_df, stu_id))


def question_senti(input_df):
    """page for individual question's sentiment"""
    select_preprocess = preprocessed_df[
        preprocessed_df[assign_id].isin(assignments)
    ].dropna(axis=1, how="all")
    questions = st.multiselect(
        label="Select specific questions below:",
        options=select_preprocess.columns[2:],
    )
    select_text = []
    for column in questions:
        select_text.append(input_df[column].to_string(index=False, na_rep=""))
    questions_senti_df = pd.DataFrame(
        {"questions": questions, "text": select_text}
    )
    # calculate overall sentiment from the combined text
    questions_senti_df[cts.SENTI] = questions_senti_df["text"].apply(
        lambda x: TextBlob(x).sentiment.polarity
    )
    if len(select_text) != 0:
        st.altair_chart(vis.question_senti_barplot(questions_senti_df))


def summary():
    """Display summarization"""
    sum_df = preprocessed_df[
        preprocessed_df[assign_id].isin(assignments)
    ].dropna(axis=1, how="all")
    for column in preprocessed_df.columns[2:]:
        sum_df[column] = preprocessed_df[column].apply(
            lambda x: sz.summarize_text(x)
        )
    st.write(sum_df)


def tpmodel():
    """Display topic modeling"""
    topic_df = main_df.copy(deep=True)
    topic_df = topic_df[topic_df[assign_id].isin(assignments)]
    # st.write(topic_df)
    tp_type = st.sidebar.selectbox(
        "Type of topic modeling analysis", ["Histogram", "Scatter"]
    )
    topic_range = st.sidebar.slider(
        "Select the amount of topics", 1, 10, value=5
    )
    word_range = st.sidebar.slider(
        "Select the amount of words per topic", 1, 10, value=5
    )
    # topic_df["topics"] = topic_df["tokens"].apply(
    #     lambda x: tm.topic_model(
    #         x, NUM_TOPICS=topic_range, NUM_WORDS=word_range)
    # )
    overall_topic_df, lda_model, corpus = tm.topic_model(
        topic_df[cts.TOKEN].tolist(),
        num_topics=topic_range,
        num_words=word_range,
    )
    overall_topic_df["Student"] = topic_df[stu_id].tolist()
    overall_topic_df[assign_id] = topic_df[assign_id].tolist()
    # reorder the column
    overall_topic_df = overall_topic_df[
        [
            assign_id,
            "Student",
            "Dominant_Topic",
            "Topic_Keywords",
            "Text",
            "Perc_Contribution",
        ]
    ]
    st.header(f"Overall topics in **{assign_text}**")
    if tp_type == "Histogram":
        hist_tm(overall_topic_df)
    elif tp_type == "Scatter":
        # topics = lda_model.show_topics(formatted=False)
        scatter_tm(lda_model, corpus, overall_topic_df)


def hist_tm(topic_df):
    """Topic modeling in histogram"""
    st.write(topic_df)
    st.altair_chart(vis.tp_hist_plot(topic_df))


def scatter_tm(lda_model, corpus, overall_topic_df):
    """Topic modeling in scatter plot"""
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

    random_state = st.sidebar.slider("Select random_state", 1, 1000, value=500)

    angle = st.sidebar.slider("Select angle", 0, 100, value=50)

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

    lda_scatter = vis.tp_scatter_plot(df_tsne)
    st.altair_chart(lda_scatter)


def doc_sim():
    """Display document similarity"""
    doc_df = main_df.copy(deep=True)
    doc_sim_type = st.sidebar.selectbox(
        "Type of similarity analysis", ["TF-IDF", "Spacy"]
    )
    st.header(
        f"Similarity between each student's document in **{assign_text}**"
    )
    if doc_sim_type == "TF-IDF":
        tf_idf_sim(doc_df)
    elif doc_sim_type == "Spacy":
        spacy_sim(doc_df)


def tf_idf_sim(doc_df):
    for assignment in assignments:
        doc = doc_df[doc_df[assign_id] == assignment].dropna(
            axis=1, how="all"
        )

        pairs = ds.create_pair(doc[stu_id])
        # calculate similarity of the docs of the selected author pairs
        similarity = [
            ds.tfidf_cosine_similarity(
                (
                    doc[doc[stu_id] == pair[0]][cts.NORMAL].values[0],
                    doc[doc[stu_id] == pair[1]][cts.NORMAL].values[0],
                )
            )
            for pair in pairs
        ]
        df_sim = pd.DataFrame({"pair": pairs, "similarity": similarity})
        # Split the pair tuple into two columns for plotting
        df_sim[["doc_1", "doc_2"]] = pd.DataFrame(
            df_sim["pair"].tolist(), index=df_sim.index
        )
        st.altair_chart(
            vis.doc_sim_heatmap(df_sim).properties(title=assignment)
        )


def spacy_sim(doc_df):
    spacy_model = st.sidebar.selectbox("Model name", SPACY_MODEL_NAMES)
    nlp = load_model(spacy_model)
    for assignment in assignments:
        doc = doc_df[doc_df[assign_id] == assignment].dropna(
            axis=1, how="all"
        )

        pairs = ds.create_pair(doc[stu_id])
        # calculate similarity of the docs of the selected author pairs
        similarity = [
            ds.spacy_doc_similarity(
                nlp,
                (
                    doc[doc[stu_id] == pair[0]][cts.NORMAL].values[0],
                    doc[doc[stu_id] == pair[1]][cts.NORMAL].values[0],
                ),
            )
            for pair in pairs
        ]
        df_sim = pd.DataFrame({"pair": pairs, "similarity": similarity})
        # Split the pair tuple into two columns for plotting
        df_sim[["doc_1", "doc_2"]] = pd.DataFrame(
            df_sim["pair"].tolist(), index=df_sim.index
        )
        st.altair_chart(
            vis.doc_sim_heatmap(df_sim).properties(title=assignment)
        )


def interactive():
    """Page to allow nlp analysis from user input"""
    input_text = st.text_area("Enter text", "Type here")
    token_cb = st.checkbox("Show tokens")
    ner_cb = st.checkbox("Show named entities")
    sentiment_cb = st.checkbox("Show sentiment")
    summary_cb = st.checkbox("Show Summary")

    # st.success("Running Analysis")
    # if st.button("Analysis"):
    if token_cb:
        tokens = az.tokenize(input_text)
        st.write(tokens)
    if ner_cb:
        doc = az.get_nlp(input_text)
        named_entities = az.named_entity_recognization(input_text)
        if len(named_entities) > 0:
            html = spacy.displacy.render(doc, style="ent")
            # Newlines seem to mess with the rendering
            html = html.replace("\n", " ")
            HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid \
        #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">\
        {}</div>"""
            st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)
        else:
            st.info("No named entity recognized")
    if sentiment_cb:
        sentiments = TextBlob(az.lemmatized_text(input_text))
        st.write(sentiments.sentiment)
    if summary_cb:
        summaries = sz.summarize_text(input_text)
        st.write(summaries)


def grammar_analyzer():
    '''Display grammar checker'''
    """page for grammar error checker"""

    ga_df = preprocessed_df[
        preprocessed_df[assign_id].isin(assignments)
    ].dropna(axis=1, how="all")
    # plot all the subplots of different assignments
    for column in preprocessed_df.columns[2:]:
        ga_df[column] = preprocessed_df[column].apply(
            lambda x: ga.grammar_analyzer(x)
        )
    st.write(ga_df)

    #TODO: for visualization team, Adam + Kevin,
    # to add the code to display the result of Grammar checker
    # Can look at how summary is displaying as a suggestion.
if __name__ == "__main__":
    main()
