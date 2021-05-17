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


def return_student_assignment(
    input_df, students, assignments, assign_id, stu_id
):
    """return entries of selected student in selected assignment in dataframe"""
    return input_df[
        (input_df[stu_id].isin(students))
        & input_df[assign_id].isin(assignments)
    ]


def return_assignments(input_df, column_name, selected):
    return input_df[input_df[column_name].isin(selected)].dropna(
        axis="columns", how="all"
    )


def return_assignment(input_df, column_name, selected):
    return input_df[input_df[column_name] == selected].dropna(
        axis="columns", how="all"
    )


def return_matched_rows(input_df, column_name, selected):
    """return rows where value of column matched with selected"""
    return input_df.loc[input_df[column_name].isin(selected)]


def return_matched_row(input_df, stu_id, student, assign_id, assignment):
    """return row that match student and assignment value"""
    return input_df.loc[
        (input_df[stu_id] == student) & (input_df[assign_id] == assignment)
    ]


def matched_row(input_df, assign_id, assignment):
    """return row that match student and assignment value"""
    return input_df.loc[input_df[assign_id] == assignment]


def return_question(question_df, question):
    return (
        return_assignment(question_df, "question", question)
        .loc[:, ["text"]]
        .to_string()
    )


def compute_freq_df(
    main_df, students, assignments, assign_id, stu_id, freq_range
):
    """
    return:
    DataFrame
    word|freq|assignments|student
    ----|----|-----------|-------
    """
    freq_df = pd.DataFrame()
    stu_assignment = return_student_assignment(
        main_df, students, assignments, assign_id, stu_id
    )
    for student in students:
        for assignment in assignments:
            try:
                # extract matching combined string
                combined_string = return_matched_row(
                    stu_assignment, stu_id, student, assign_id, assignment
                )[cts.COMBINED].item()
                # calculate word frequency
                single_freq = az.word_frequency(
                    combined_string,
                    freq_range,
                )
                single_df = freq_to_df(single_freq, assignment, student)
                freq_df = freq_df.append(single_df)
            except ValueError:
                # no matching result of student and assignment
                continue
    return freq_df


def freq_to_df(freq_lst, assignment, student):
    """
    return:
    DataFrame
    word|freq|assignments|student
    ----|----|-----------|-------
    """
    single_freq_df = pd.DataFrame(freq_lst, columns=["word", "freq"])
    single_freq_df["assignments"] = assignment
    single_freq_df["student"] = student
    return single_freq_df


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


def compute_quest_df(questions, freq_range, question_df):
    freq_question_df = pd.DataFrame(columns=["question", "word", "freq"])
    for question in questions:
        quest_freq = az.word_frequency(
            return_question(question_df, question),
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
    doc = return_assignment(doc_df, assign_id, assignment)

    pairs = ds.create_pair(doc[stu_id])
    # calculate similarity of the docs of the selected author pairs
    if model == "tfidf":
        similarity = [
            ds.tfidf_cosine_similarity(make_tuple(doc, stu_id, pair))
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


def make_freq_df(assignments, main_df, assign_id, freq_range):
    freq_df = pd.DataFrame(columns=["assignments", "word", "freq"])
    # calculate word frequency of each assignments
    for assignment in assignments:
        # combined text of the whole assignment
        combined_text = " ".join(
            return_assignment(main_df, assign_id, assignment)[cts.NORMAL]
        )
        item_df = pd.DataFrame(
            az.word_frequency(combined_text, freq_range),
            columns=["word", "freq"],
        )
        item_df["assignments"] = assignment
        freq_df = freq_df.append(item_df)
    return freq_df


def make_summary_df(assignment, input_df, assign_id):
    sum_assignment_df = return_assignment(input_df, assign_id, assignment)
    for column in sum_assignment_df.columns[2:]:
        sum_assignment_df[column] = sum_assignment_df[column].apply(
            lambda x: sz.summarize_text(x)
        )
    return sum_assignment_df
