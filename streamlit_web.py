import streamlit as st
import pandas as pd
import altair as alt
from textblob import TextBlob

import src.analyzer as az
import src.markdown as md

from typing import List, Tuple

directory = "resources/cs100f2019_lab05_reflections"
df = pd.DataFrame(md.collect_md(directory))


def main():

    # Title
    st.sidebar.title("What to do")

    analysis_mode = st.sidebar.selectbox(
        "Choose the analysis mode", ["Home", "Frequency Analysis", "Sentiment Analysis"]
    )
    if analysis_mode == "Home":
        with open("README.md") as readme_file:
            st.markdown(readme_file.read())
    if analysis_mode == "Frequency Analysis":
        st.title("Frequency Analysis")
        frequency()
    elif analysis_mode == "Sentiment Analysis":
        st.title("Sentiment Analysis")
        sentiment()


def frequency():
    freq_type = st.sidebar.selectbox(
        "Type of frequency analysis", ["Overall", "Student", "Question"]
    )
    freq_range = st.sidebar.slider(
        "Select a range of Most frequent words?", 1, 50, value=25
    )
    if freq_type == "Overall":
        st.sidebar.success(
            'To continue see individual frequency analysis select "Individual"'
        )
        st.header("Overall most frequent words in the directory")
        overall_freq(freq_range)
    elif freq_type == "Student":
        st.header("Most frequent words by individual students")
        individual_student_freq(df, freq_range)
    elif freq_type == "Question":
        st.header("Most frequent words in individual questions")
        individual_question_freq(df, freq_range)


def sentiment():
    df_combined = combine_column_text(df)
    # calculate overall sentiment from the combined text
    df_combined["sentiment"] = df_combined["combined"].apply(
        lambda x: TextBlob(x).sentiment.polarity
    )
    senti_type = st.sidebar.selectbox(
        "Type of sentiment analysis", ["Overall", "Student", "Question"]
    )
    if senti_type == "Overall":
        st.sidebar.success(
            'To continue see individual frequency analysis select "Individual"'
        )
        st.header("Overall sentiment polarity in the directory")
        overall_senti(df_combined)
    elif senti_type == "Student":
        st.header("View sentiment by individual students")
        individual_student_senti(df_combined)
    elif senti_type == "Question":
        st.header("View sentiment by individual questions")


def overall_freq(freq_range):

    plot_frequency(az.dir_frequency(directory, freq_range))


def combine_column_text(raw_df):
    df_combined = raw_df
    # filter out first column -- user info
    cols = df_combined.columns[1:]
    # combining text into combined column
    df_combined["combined"] = df_combined[cols].apply(
        lambda row: " ".join(row.values.astype(str)), axis=1
    )

    return df_combined


def overall_senti(senti_df):

    senti_hist = (
        alt.Chart(senti_df)
        .mark_bar()
        .encode(
            alt.X("sentiment", bin=True),
            y="count()",
            opacity=alt.value(0.7),
            color=alt.value("blue"),
        )
    )
    senti_point = (
        alt.Chart(senti_df)
        .mark_point()
        .encode(
            x="Reflection by",
            y="sentiment",
            color="Reflection by",
            tooltip=[
                alt.Tooltip("sentiment", title="polarity"),
                alt.Tooltip("Reflection by", title="author"),
            ],
        )
    )

    st.altair_chart(senti_hist)
    st.altair_chart(senti_point)


def individual_student_senti(df):
    students = st.multiselect(
        label="Select specific students below:", options=df["Reflection by"]
    )
    df_selected_stu = df.loc[df["Reflection by"].isin(students)]
    senti_df = pd.DataFrame(df_selected_stu, columns=["Reflection by", "sentiment"])
    st.write(senti_df)

    senti_plot = (
        alt.Chart(senti_df)
        .mark_bar()
        .encode(
            alt.Y("Reflection by", title="Student", sort="-x"),
            alt.X("sentiment", title="Sentiment"),
            tooltip=[alt.Tooltip("sentiment", title="Sentiment")],
            opacity=alt.value(0.7),
            color=alt.value("red"),
        )
    )

    st.altair_chart(senti_plot)


def individual_student_freq(df_combined, freq_range):
    # filter out first column -- user info
    cols = df_combined.columns[1:]
    # combining text into combined column
    df_combined["combined"] = df_combined[cols].apply(
        lambda row: " ".join(row.values.astype(str)), axis=1
    )
    # st.write(df_combined)
    students = st.multiselect(
        label="Select specific students below:", options=df_combined["Reflection by"]
    )
    # plot based on student selected
    if students != "":
        for student in students:
            plot_frequency(
                az.word_frequency(
                    df_combined[df_combined["Reflection by"] == student]
                    .loc[:, ["combined"]]
                    .to_string(),
                    freq_range,
                )
            )


def individual_question_freq(df, freq_range):
    st.write(df)
    questions = st.multiselect(
        label="Select specific questions below:", options=df.columns[1:]
    )
    select_text = ""
    for column in questions:
        select_text += df[column].to_string(index=False)
    if select_text != "":
        plot_frequency(az.word_frequency(select_text, freq_range))


def plot_frequency(data: List[Tuple[str, int]]):
    freq_df = pd.DataFrame(data, columns=["word", "freq"])
    # st.write(freq_df)

    freq_plot = (
        alt.Chart(freq_df)
        .mark_bar()
        .encode(
            alt.Y("word", title="words", sort="-x"),
            alt.X("freq", title="frequencies"),
            tooltip=[alt.Tooltip("freq", title="frequency")],
            opacity=alt.value(0.7),
            color=alt.value("blue"),
        )
    )

    # st.bar_chart(freq_df)
    st.altair_chart(freq_plot)


if __name__ == "__main__":
    main()
