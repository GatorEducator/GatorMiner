import altair as alt
import pandas as pd
import streamlit as st

from typing import List, Tuple


def plot_overall_senti(senti_df, student_id):
    """Visulize overall sentiment with histogram and scatter plots"""
    senti_hist = (
        alt.Chart(senti_df)
        .mark_bar()
        .encode(
            alt.Y("sentiment", bin=True),
            x="count()",
            color="sentiment",
        ).properties(
            height=300,
            width=100
        )
    )
    senti_point = (
        alt.Chart(senti_df)
        .mark_circle(size=300, fillOpacity=0.7)
        .encode(
            alt.X(student_id),
            alt.Y("sentiment"),
            alt.Color(student_id, legend=alt.Legend(orient="left")),
            tooltip=[
                alt.Tooltip("sentiment", title="polarity"),
                alt.Tooltip(student_id, title="author"),
            ],
        )
    )
    combine = alt.hconcat(senti_point, senti_hist)
    st.altair_chart(combine)


def plot_student_sentiment(senti_df, student_id):
    """plot sentiment by student from a df containing name and senti"""
    senti_plot = (
        alt.Chart(senti_df)
        .mark_bar()
        .encode(
            alt.Y(student_id, title="Student", sort="-x"),
            alt.X("sentiment", title="Sentiment"),
            tooltip=[alt.Tooltip("sentiment", title="Sentiment")],
            opacity=alt.value(0.7),
            color=student_id,
        ).properties(width=700, height=450)
    )

    st.altair_chart(senti_plot)


def plot_question_sentiment(senti_df):
    """plot sentiment by student from a df containing name and senti"""
    senti_plot = (
        alt.Chart(senti_df)
        .mark_bar()
        .encode(
            alt.Y("questions", title="Questions", sort="-x"),
            alt.X("sentiment", title="Sentiment"),
            tooltip=[alt.Tooltip("sentiment", title="Sentiment")],
            opacity=alt.value(0.7),
            color=alt.condition(
                alt.datum.sentiment > 0,
                alt.value("steelblue"),
                alt.value("red")
            )
        ).properties(width=700, height=450)
    )

    st.altair_chart(senti_plot)


def plot_frequency(data: List[Tuple[str, int]]):
    """function to plot word frequency"""
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
        ).properties(title='frequency plot')
    )

    # st.bar_chart(freq_df)
    st.altair_chart(freq_plot)
