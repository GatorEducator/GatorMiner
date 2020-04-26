import altair as alt
from altair.expr import datum
import pandas as pd
import streamlit as st


def senti_combinedplot(senti_df, student_id):
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


def stu_senti_barplot(senti_df, student_id):
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


def question_senti_barplot(senti_df):
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


def freq_barplot(freq_df):
    """function to plot word frequency"""
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


def doc_sim_heatmap(df_sim):
    heatmap = alt.Chart(df_sim).mark_rect().encode(
        x=alt.X('doc_1', sort=None, title="student"),
        y=alt.Y('doc_2', sort="-x", title="student"),
        color='similarity',
        tooltip=[
            alt.Tooltip("similarity", title="similarity"),
        ]
    ).properties(width=600, height=550)
    st.altair_chart(heatmap)


def stu_freq_barplot(freq_df, students):
    base = alt.Chart(freq_df).mark_bar().encode(
        alt.X('freq', title=None),
        alt.Y('word', title=None, sort="-x"),
        tooltip=[
            alt.Tooltip("freq", title="frequency"),
            alt.Tooltip("word", title="word"),
        ],
        opacity=alt.value(0.7),
        color=alt.Color('student', legend=None)
        ).properties(
            width=190,
        )

    subplts = []
    for stu in students:
        subplts.append(
            base.transform_filter(datum.student == stu).properties(title=stu))

    grid = facet_wrap(subplts)
    st.altair_chart(grid)


def facet_wrap(subplts, plots_per_row=3):
    row_stu = [subplts[i: i + plots_per_row]
               for i in range(0, len(subplts), plots_per_row)]
    column_plot = alt.vconcat(spacing=10)
    for row in row_stu:
        row_plot = alt.hconcat(spacing=10)
        for item in row:
            row_plot |= item
        column_plot &= row_plot

    return column_plot
