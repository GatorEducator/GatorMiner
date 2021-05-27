"""Pandas related util functions."""
import pandas as pd

from textblob import TextBlob

from . import analyzer as az
from . import constants as cts
from . import doc_similarity as ds
from . import summarizer as sz


def return_student_assignment(
    input_df, student, assignment, assign_id, stu_id
):
    """Return entries of selected student and assignment in dataframe."""
    if isinstance(student, list) & isinstance(assignment, list):
        return input_df[
            (input_df[stu_id].isin(student))
            & input_df[assign_id].isin(assignment)
        ]
    elif isinstance(student, str) & isinstance(assignment, str):
        return input_df[
            (input_df[stu_id] == student) & (input_df[assign_id] == assignment)
        ]
    else:
        raise TypeError(f"{student} or {assignment} is not list or str type")


def return_assignment(input_df, column_name, selected):
    """Return entries where one column matches with selected in dataframe."""
    if isinstance(selected, list):
        # a list of selected assignments
        return input_df[input_df[column_name].isin(selected)].dropna(
            axis="columns", how="all"
        )
    elif isinstance(selected, str):
        # one selected assignment
        return input_df[input_df[column_name] == selected].dropna(
            axis="columns", how="all"
        )
    else:
        raise TypeError(f"{selected} is not list or str type")


def compute_freq_df(
    main_df, students, assignments, assign_id, stu_id, freq_range
):
    """Compute freq and return in dataframe.

    Return:
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
                combined_string = return_student_assignment(
                    stu_assignment,
                    student,
                    assignment,
                    assign_id,
                    stu_id,
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
    """ Make freq list into dataframe.

    Return:
    DataFrame
    word|freq|assignments|student
    ----|----|-----------|-------
    """
    single_freq_df = pd.DataFrame(freq_lst, columns=["word", "freq"])
    single_freq_df["assignments"] = assignment
    single_freq_df["student"] = student
    return single_freq_df


def make_questions_df(questions, main_df):
    """Make selected questions into a dataframe."""
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
    """Compute freq of questions and return dataframe."""
    freq_question_df = pd.DataFrame(columns=["question", "word", "freq"])
    for question in questions:
        quest_df = (
            return_assignment(question_df, "question", question)
            .loc[:, ["text"]]
            .to_string()
        )
        quest_freq = az.word_frequency(
            quest_df,
            freq_range,
        )
        ind_df = pd.DataFrame(quest_freq, columns=["word", "freq"])
        ind_df["question"] = question
        freq_question_df = freq_question_df.append(ind_df)
    return freq_question_df


def compute_question_senti(questions, input_df):
    """Compute question sentiment score."""
    select_text = []
    # list of all responses of individual questions combined
    for question in questions:
        combined = input_df[question].to_string(index=False, na_rep="")
        select_text.append(combined)
    questions_senti_df = pd.DataFrame(
        {"questions": questions, "text": select_text}
    )
    # calculate overall sentiment from the combined text
    questions_senti_df[cts.SENTI] = questions_senti_df["text"].apply(
        lambda x: TextBlob(x).sentiment.polarity
    )
    return select_text, questions_senti_df


def sim_pair(assignment, doc_df, assign_id, stu_id, model, nlp=None):
    """Compute similarity score between pairs and return in dataframe."""
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
    """Make pair into tuples."""
    return (
        doc[doc[stu_id] == pair[0]][cts.NORMAL].values[0],
        doc[doc[stu_id] == pair[1]][cts.NORMAL].values[0],
    )


def make_freq_df(assignments, main_df, assign_id, freq_range):
    """Compute frequency and return result in dataframe."""
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
    """Summarize and return in dataframe."""
    sum_assignment_df = return_assignment(input_df, assign_id, assignment)
    for column in sum_assignment_df.columns[2:]:
        sum_assignment_df[column] = sum_assignment_df[column].apply(
            lambda x: sz.summarize_text(x)
        )
    return sum_assignment_df
