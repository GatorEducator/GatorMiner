"""Web interface"""

import re
import base64
import numpy as np
import os
import pandas as pd
from sklearn.manifold import TSNE
import spacy
from spacy import displacy
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
import src.utils as ut


# resources/sample_reflections/lab1, resources/sample_reflections/lab2

# initialize main_df
SPACY_MODEL_NAMES = ["en_core_web_sm", "en_core_web_md"]
main_df = pd.DataFrame()
selected_df = pd.DataFrame()
selected_nan_df = pd.DataFrame()
assignments = None
assignment_string = None
stu_id = None
assign_id = None
success_msg = None
debug_mode = True
main_md_dict = None


def main():
    """main streamlit function"""
    # Title
    st.sidebar.title("Welcome to GatorMiner!")
    data_retreive_method = st.sidebar.selectbox(
        "Choose the data retrieving method",
        [
            "Path input",
            "AWS",
            "Upload local files",
        ],
    )
    if retreive_data(data_retreive_method):
        analysis_mode = st.sidebar.selectbox(
            "Choose the analysis mode",
            [
                "Home",
                "Frequency Analysis",
                "Sentiment Analysis",
                "Entity Analysis",
                "Document Similarity",
                "Summary",
                "Topic Modeling",
                "Interactive",
            ],
        )
        if debug_mode:
            st.write(main_df)
        if analysis_mode == "Home":
            landing_src()
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
            elif analysis_mode == "Entity Analysis":
                st.title(analysis_mode)
                entities()
            success_msg.empty()


def landing_src():
    """function to load and configurate readme source"""

    with open("docs/LANDING_PAGE.md") as landing_file:
        landing_src = landing_file.read()
        for file in os.listdir(cts.IMG_DIR):
            if file.endswith(".png"):
                img_path = f"{cts.IMG_DIR}{os.path.sep}{file}"
                with open(img_path, "rb") as f:
                    img_bin = base64.b64encode(f.read()).decode()
                landing_src = landing_src.replace(
                    img_path, f"data:image/png;base64,{img_bin}"
                )

        st.markdown(landing_src, unsafe_allow_html=True)


def landing_pg():
    """landing page"""
    landing = st.sidebar.selectbox("Welcome", ["Home", "Interactive"])

    if landing == "Home":
        landing_src()
    else:
        interactive()


def retreive_data(data_retreive):
    """pipeline to retrieve data from user input to output"""
    global main_df
    if data_retreive == "Path input":
        input_assignments = st.sidebar.text_input(
            "Enter path(s) to markdown documents (seperate by comma)"
        )
    elif data_retreive == "AWS":
        input_assignments = st.sidebar.text_input(
            "Enter assignment names of the markdown \
documents(seperate by comma)"
        )
        st.sidebar.info(
            "You will need to store keys and endpoints in the \
environment variables"
        )
    else:
        input_assignments = st.sidebar.file_uploader(
            "Choose a Markdown file", type=["md"], accept_multiple_files=True
        )
    if not input_assignments:
        landing_pg()
    else:
        if data_retreive == "AWS" or data_retreive == "Path input":
            input_assignments = re.split(r"[;,\s]\s*", input_assignments)
        try:
            raw_df, main_df = import_data(data_retreive, input_assignments)
        except TypeError:
            st.sidebar.warning(
                "No data imported. Please check the reflection document input"
            )
            landing_src()
        else:
            global success_msg
            global assign_id
            global assignments
            global assignment_string
            global stu_id
            global selected_nan_df
            global selected_df
            success_msg = None
            if main_df.empty is not True:
                success_msg = st.sidebar.success("Sucessfully Loaded!!")
            # Column name of assignment and student names
            assign_id = main_df.columns[0]
            stu_id = main_df.columns[1]
            # selected assignments
            assignments = st.sidebar.multiselect(
                label="Select assignments below:",
                options=main_df[assign_id].unique(),
            )
            selected_nan_df = ut.return_assignments(raw_df, assign_id, assignments)
            selected_df = ut.return_assignments(main_df, assign_id, assignments)
            # string display of the selected assignments
            assignment_string = ", ".join(assignments)
            return True


@st.cache(allow_output_mutation=True)
def load_model(name):
    """load spacy model"""
    return spacy.load(name)


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def import_data(data_retreive_method, paths):
    """pipeline to import data from local or aws"""
    json_lst = []
    global main_md_dict
    if data_retreive_method == "Path input":
        try:
            for path in paths:
                json_lst.append(md.collect_md(path))
        except FileNotFoundError as err:
            st.sidebar.text(err)
            with open("README.md") as readme_file:
                st.markdown(readme_file.read())
    elif data_retreive_method == "AWS":
        passbuild = st.sidebar.checkbox(
            "Only retreive build success records", value=True
        )
        try:
            configs = gh.auth_config()
            for path in paths:
                response = gh.get_request(path, passbuild, **configs)
                json_lst.append(ju.clean_report(response))
        except (EnvironmentError, Exception) as err:
            st.sidebar.error(err)
            with open("README.md") as readme_file:
                st.markdown(readme_file.read())
    else:
        try:
            if len(paths) < 2:
                st.sidebar.warning("Please select more than one file!")
            else:
                json_lst.append(md.import_uploaded_files(paths))
        except FileNotFoundError as err:
            st.sidebar.text(err)
            with open("README.md") as readme_file:
                st.markdown(readme_file.read())
    # when data is retreived
    if json_lst:
        raw_df = pd.DataFrame()
        processed_df = pd.DataFrame()
        for item in json_lst:
            single_df = pd.DataFrame(item)
            # NA as `nan`
            raw_df = pd.concat([raw_df, single_df])
        # NA as ""
        processed_df = raw_df.fillna("")
        df_preprocess(processed_df)
        return raw_df, processed_df


def df_preprocess(df):
    """build and preprocess (combine, normalize, tokenize) text"""
    # filter out first two columns -- non-report content
    # (student and assignment name)
    cols = df.columns[2:]
    # combining text into combined column
    df[cts.COMBINED] = df[cols].apply(
        lambda row: "\n".join(row.values.astype(str)), axis=1
    )
    # normalize
    df[cts.NORMAL] = df[cts.COMBINED].apply(lambda row: az.normalize(row))
    # tokenize
    df[cts.TOKEN] = df[cts.NORMAL].apply(lambda row: az.tokenize(row))


def frequency():
    """main function for frequency analysis"""
    freq_type = st.sidebar.selectbox(
        "Type of frequency analysis", ["Overall", "Student", "Question"]
    )
    range_select_msg = "Select a range of most frequent words"
    freq_msg = "Most frequent words"
    if freq_type == "Overall":
        freq_range = st.sidebar.slider(range_select_msg, 1, 50, value=25)
        st.sidebar.success(
            'To continue see individual frequency analysis select "Student"'
        )
        st.header(f"{freq_msg} in **{assignment_string}**")
        overall_freq(freq_range)
    elif freq_type == "Student":
        freq_range = st.sidebar.slider(range_select_msg, 1, 20, value=10)
        st.header(
            f"{freq_msg} by individual students in **{assignment_string}**"
        )
        student_freq(freq_range)
    elif freq_type == "Question":
        freq_range = st.sidebar.slider(range_select_msg, 1, 20, value=10)
        st.header(
            f"{freq_msg} in individual questions in **{assignment_string}**"
        )
        question_freq(freq_range)


def overall_freq(freq_range):
    """page fore overall word frequency"""
    plots_range = st.sidebar.slider(
        "Select the number of plots per row", 1, 5, value=3
    )
    freq_df = ut.make_freq_df(assignments, main_df, assign_id, freq_range)
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
        options=selected_df[stu_id].unique(),
    )

    plots_range = st.sidebar.slider(
        "Select the number of plots per row", 1, 5, value=3
    )
    if len(students) != 0:
        freq_df = ut.compute_freq_df(
            main_df, students, assignments, assign_id, stu_id, freq_range
        )

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
    questions = st.multiselect(
        label="Select specific questions below:",
        options=selected_nan_df.columns[2:],
    )

    plots_range = st.sidebar.slider(
        "Select the number of plots per row", 1, 5, value=1
    )

    question_df = ut.make_questions_df(questions, main_df)
    if len(questions) != 0:
        freq_question_df = ut.compute_quest_df(
            questions, freq_range, question_df
        )

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
    # Initializing the new columns with a numpy array, so the entire series is returned
    senti_df[cts.POSITIVE], senti_df[cts.NEGATIVE] = az.top_polarized_word(
        senti_df[cts.TOKEN].values
    )

    # calculate overall sentiment from the combined text
    senti_df[cts.SENTI] = senti_df["combined"].apply(
        lambda x: TextBlob(az.lemmatized_text(x)).sentiment.polarity
    )
    senti_df = ut.return_assignments(senti_df, assign_id, assignments)
    senti_type = st.sidebar.selectbox(
        "Type of sentiment analysis", ["Overall", "Student", "Question"]
    )
    if senti_type == "Overall":
        st.sidebar.success(
            'To continue see individual sentiment analysis select "Student"'
        )
        st.header(f"Overall sentiment polarity in **{assignment_string}**")
        overall_senti(senti_df)
    elif senti_type == "Student":
        st.header(
            f"View sentiment by individual students in **{assignment_string}**"
        )
        student_senti(senti_df)
    elif senti_type == "Question":
        st.header(
            f"View sentiment by individual questions in **{assignment_string}**"
        )
        question_senti(senti_df)


def overall_senti(input_df):
    """page for overall senti"""
    # display line plot when there are multiple assingments
    if len(assignments) > 1:
        st.altair_chart(vis.stu_senti_lineplot(input_df, stu_id))
    st.altair_chart((vis.senti_combinedplot(input_df, stu_id)))


def student_senti(input_df):
    """page for display individual student's sentiment"""
    students = st.multiselect(
        label="Select specific students below:",
        options=input_df[stu_id].unique(),
    )
    plots_range = st.sidebar.slider(
        "Select the number of plots per row", 1, 5, value=3
    )
    df_selected_stu = ut.return_matched_rows(input_df, stu_id, students)
    if len(students) != 0:
        st.altair_chart(
            vis.facet_senti_barplot(
                df_selected_stu, students, stu_id, plots_per_row=plots_range
            )
        )
        st.altair_chart(vis.stu_senti_barplot(df_selected_stu, stu_id))


def question_senti(input_df):
    """page for individual question's sentiment"""
    questions = st.multiselect(
        label="Select specific questions below:",
        options=selected_nan_df.columns[2:],
    )
    select_text, questions_senti_df = ut.question_senti_select(
        questions, input_df
    )
    if len(select_text) != 0:
        st.altair_chart(vis.question_senti_barplot(questions_senti_df))


def summary():
    """Display summarization"""
    sum_df = ut.return_assignments(main_df, assign_id, assignments)
    for column in main_df.columns[2:]:
        sum_df[column] = main_df[column].apply(lambda x: sz.summarize_text(x))
    st.write(sum_df)


def tpmodel():
    """Display topic modeling"""
    topic_df = main_df.copy(deep=True)
    topic_df = ut.return_assignments(topic_df, assign_id, assignments)
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
    st.header(f"Overall topics in **{assignment_string}**")
    if tp_type == "Histogram":
        hist_tm(overall_topic_df)
    elif tp_type == "Scatter":
        # topics = lda_model.show_topics(formatted=False)
        scatter_tm(lda_model, corpus, overall_topic_df)


def hist_tm(topic_df):
    """Topic modeling in histogram"""
    # st.write(topic_df)
    st.altair_chart(vis.tp_hist_plot(topic_df))


def scatter_tm(lda_model, corpus, overall_topic_df):
    """Topic modeling in scatter plot"""

    random_state = st.sidebar.slider("Select random_state", 1, 1000, value=500)

    angle = st.sidebar.slider("Select angle", 0, 100, value=50)

    df_tsne = tm.tsne(lda_model, corpus, overall_topic_df, random_state, angle)

    lda_scatter = vis.tp_scatter_plot(df_tsne)
    st.altair_chart(lda_scatter)


def doc_sim():
    """Display document similarity"""
    doc_df = main_df.copy(deep=True)
    doc_sim_type = st.sidebar.selectbox(
        "Type of similarity analysis", ["TF-IDF", "Spacy"]
    )
    st.header(
        f"Similarity between each student's document in **{assignment_string}**"
    )
    if doc_sim_type == "TF-IDF":
        tf_idf_sim(doc_df)
    elif doc_sim_type == "Spacy":
        spacy_sim(doc_df)


def tf_idf_sim(doc_df):
    for assignment in assignments:
        df_sim = ut.sim_pair(assignment, doc_df, assign_id, stu_id, "tfidf")
        st.altair_chart(
            vis.doc_sim_heatmap(df_sim).properties(title=assignment)
        )


def spacy_sim(doc_df):
    spacy_model = st.sidebar.selectbox("Model name", SPACY_MODEL_NAMES)
    nlp = load_model(spacy_model)
    for assignment in assignments:
        df_sim = ut.sim_pair(
            assignment, doc_df, assign_id, stu_id, "spacy", nlp
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
        displacy_renderer(az.get_nlp(input_text))
    if sentiment_cb:
        sentiments = TextBlob(az.lemmatized_text(input_text))
        st.write(sentiments.sentiment)
    if summary_cb:
        summaries = sz.summarize_text(input_text)
        st.write(summaries)


def entities():
    """Page to display entity analysis"""
    st.write(
        "Entity analysis inspects the given text for known entities \
    and returns information about those entities. It is a way to extract \
    information that seeks to locate and classify named entities in text \
    into pre-defined categories such as the names of persons, organizations, \
    locations, expressions of times, quantities, monetary values, and percentages."
    )

    # make a copy of the main dataframe

    # makes a drop down list to select users classified by assignments
    for assignment in assignments:
        st.write("")
        st.subheader(assignment)
        df_selected_assign = ut.matched_row(selected_df, assign_id, assignment)
        for student in df_selected_assign[stu_id].unique():
            with st.beta_expander(student):
                entity_analysis(assignment, student, selected_df)


def entity_analysis(assignment, student, input_df):
    """function that selects, modifies and runs the entity analysis on a document"""
    # makes a dataframe with the selected user's information
    df_selected_stu = ut.return_matched_row(
        input_df, stu_id, student, assign_id, assignment
    )

    # selects the combined column from the dataframe and extracts it
    combine_start = df_selected_stu.columns.get_loc("combined")
    combine_end = df_selected_stu.columns.get_loc("combined") + 1
    df_selected_stu_combined = df_selected_stu.iloc[
        :, combine_start:combine_end
    ]
    # convert the combined dataframe into a string
    student_string = df_selected_stu_combined.to_string(
        header=False, index=False
    )
    student_string = student_string.replace("\\n", "")

    # run the spacy entity recogonizer on the selected user document and display it
    doc = az.get_nlp(student_string)
    displacy_renderer(doc)


def displacy_renderer(doc):
    """runs the spacy displacy function on the given string and
    renders the output"""
    if len(doc) > 0:
        html = spacy.displacy.render(doc, style="ent")
        # Newlines seem to mess with the rendering
        html = html.replace("\n", " ")
        HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid \
    #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">\
    {}</div>"""
        st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)
    else:
        st.info("No named entity recognized")


if __name__ == "__main__":
    main()
