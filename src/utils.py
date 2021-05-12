import pandas as pd

from textblob import TextBlob

from . import analyzer as az
from . import constants as cts
from . import doc_similarity as ds
from . import get_handler as gh
from . import json_util as ju
from . import markdown as md
from . import summarizer as sz
from . import topic_modeling as tm
from . import visualization as vis


def return_student_assignment(main_df, students, assignments, assign_id, stu_id):
    """return entries of selected student in selected assignment in dataframe"""
    selected_df = main_df[
        (main_df[stu_id].isin(students))
        & main_df[assign_id].isin(assignments)
    ]
    return selected_df


def return_assignment(preprocessed_df, assign_id, assignments):
    select_preprocess = preprocessed_df[
        preprocessed_df[assign_id].isin(assignments)
    ].dropna(axis=1, how="all")
    return select_preprocess


def return_matched_rows(input_df, column_name, selected):
    """return rows where value of column matched with selected"""
    return input_df.loc[input_df[column_name].isin(selected)]


def return_matched_row(input_df, stu_id, student, assign_id, assignment):
    df_selected_stu = input_df.loc[
        input_df[stu_id].isin([student])
        & input_df[assign_id].isin([assignment])
    ]
    return df_selected_stu

def compute_freq_df(main_df, students, assignments, assign_id, stu_id, freq_range):
    freq_df = pd.DataFrame(columns=["student", "word", "freq"])
    stu_assignment = return_student_assignment(main_df, students, assignments, assign_id, stu_id)
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
            ind_df = pd.DataFrame(individual_freq,
                                    columns=["word", "freq"])
            ind_df["assignments"] = item
            ind_df["student"] = student
            freq_df = freq_df.append(ind_df)
    return freq_df


def compute_quest_df(questions, freq_range, question_df):
    freq_question_df = pd.DataFrame(columns=["question", "word", "freq"])
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
    return freq_question_df


def question_senti_select(questions, input_df):
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
    return select_text, questions_senti_df


def sim_pair(assignment, doc_df, assign_id, stu_id, model, nlp=None):
    doc = doc_df[doc_df[assign_id] == assignment].dropna(
        axis=1, how="all"
    )

    pairs = ds.create_pair(doc[stu_id])
    # calculate similarity of the docs of the selected author pairs
    if model == "tfidf":
        similarity = [
            ds.tfidf_cosine_similarity(
                make_tuple(doc, stu_id, pair)
            )
            for pair in pairs
        ]
    elif model == "spacy":
        similarity = [
            ds.spacy_doc_similarity(
                nlp,
                make_tuple(doc, stu_id, pair),
            )
            for pair in pairs
        ]
    df_sim = pd.DataFrame({"pair": pairs, "similarity": similarity})
    # Split the pair tuple into two columns for plotting
    df_sim[["doc_1", "doc_2"]] = pd.DataFrame(
        df_sim["pair"].tolist(), index=df_sim.index
    )
    return df_sim


def make_tuple(doc, stu_id, pair):
    return (
        doc[doc[stu_id] == pair[0]][cts.NORMAL].values[0],
        doc[doc[stu_id] == pair[1]][cts.NORMAL].values[0],
    )


def make_questions_df(questions, main_df):
    select_text = {}
    for question in questions:
        select_text[question] = main_df[question].to_string(
            index=False, na_rep=""
        )
    question_df = pd.DataFrame(
        select_text.items(), columns=["question", "text"]
    )
    return question_df


def make_freq_df(assignments, main_df, assign_id, freq_range):
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
    return freq_df
