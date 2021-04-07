"""Visualization used in main streamlit interface"""
import altair as alt
from altair.expr import datum

import src.constants as cts


def freq_barplot(freq_df):
    """barplot for word frequency"""
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
        .properties(title="frequency plot")
    ).interactive()

    # st.bar_chart(freq_df)
    return freq_plot


def facet_freq_barplot(
        freq_df, options, subplot_column, color_column=None, plots_per_row=3):
    """facet bar plot for word frequencies"""
    # Don't display legend if color for subplots
    if color_column is None:
        color_column = subplot_column
        legend = None
    else:
        legend = alt.Legend(title=f"{color_column} by color")

    base = (
        alt.Chart(freq_df)
        .mark_bar()
        .encode(
            alt.X("freq", title=None),
            alt.Y("word", title=None, sort="-x"),
            tooltip=[
                alt.Tooltip("freq", title="frequency"),
                alt.Tooltip("word", title="word"),
            ],
            opacity=alt.value(0.7),
            color=alt.Color(color_column, legend=legend),
        )
        .properties(width=190,)
    ).interactive()

    subplts = []
    for item in options:
        subplts.append(
            base.transform_filter(
                datum[subplot_column] == item).properties(title=item)
        )

    grid = facet_wrap(subplts, plots_per_row)

    return grid


def facet_senti_barplot(senti_df, options, column_name, plots_per_row=3):
    """facet bar plot for word frequencies"""
    base = (
        alt.Chart(senti_df)
        .mark_bar()
        .encode(
            alt.Y(cts.ASSIGNMENT, title=None),
            alt.X(cts.SENTI, title=None),
            tooltip=[
                alt.Tooltip(cts.ASSIGNMENT, title="assignment"),
                alt.Tooltip(cts.SENTI, title="sentiment"),
            ],
            opacity=alt.value(0.7),
            color=alt.Color(column_name, legend=None),
        )
        .properties(width=190,)
    ).interactive()

    subplts = []
    for item in options:
        subplts.append(
            base.transform_filter(
                datum[column_name] == item).properties(title=item)
        )

    grid = facet_wrap(subplts, plots_per_row)

    return grid


def facet_wrap(subplts, plots_per_row=3):
    """make subplots into facet based on the plot number per row"""
    row_stu = [
        subplts[i: i + plots_per_row] for i in range(
            0, len(subplts), plots_per_row
        )
    ]
    column_plot = alt.vconcat(spacing=10)
    for row in row_stu:
        row_plot = alt.hconcat(spacing=10)
        for item in row:
            row_plot |= item
        column_plot &= row_plot

    return column_plot


def senti_combinedplot(senti_df, student_id):
    """combined circle and histogram plot for sentiment"""
    combine = alt.hconcat(
        senti_circleplot(senti_df, student_id), senti_histplot(senti_df)
    )
    return combine


def senti_histplot(senti_df):
    """histogram plot for sentiment"""
    senti_hist = (
        alt.Chart(senti_df)
        .mark_bar()
        .encode(alt.Y(cts.SENTI, bin=True), x="count()", color=cts.SENTI,)
        .properties(height=300, width=100)
    ).interactive()
    return senti_hist


def senti_circleplot(senti_df, student_id):
    """circle plot for sentiment"""
    senti_circle = (
        alt.Chart(senti_df)
        .mark_point(size=100, fillOpacity=0.7)
        .encode(
            alt.X(student_id),
            alt.Y(cts.SENTI),
            alt.Color(cts.ASSIGNMENT, legend=alt.Legend(orient="left")),
            alt.Shape(cts.ASSIGNMENT, legend=None),
            tooltip=[
                alt.Tooltip(cts.SENTI, title="polarity"),
                alt.Tooltip(student_id, title="author"),
                alt.Tooltip("Positive words", title="Positive words"),
                alt.Tooltip("Negative words", title="Negative words"),
            ],
        )
    ).interactive()
    return senti_circle


def stu_senti_barplot(senti_df, student_id):
    """barplot for individual student' sentiment"""
    senti_plot = (
        alt.Chart(senti_df)
        .mark_bar()
        .encode(
            alt.Y(student_id, title="Student", sort="-x"),
            alt.X(cts.SENTI, title="Sentiment"),
            tooltip=[alt.Tooltip(cts.SENTI, title="Sentiment")],
            opacity=alt.value(0.7),
            color=cts.ASSIGNMENT,
        )
        .properties(width=700, height=450)
    ).interactive()

    return senti_plot


def stu_senti_lineplot(senti_df, student_id):
    """barplot for individual student' sentiment"""
    senti_lineplot = (
        alt.Chart(senti_df)
        .mark_line()
        .encode(x=cts.ASSIGNMENT, y=cts.SENTI, color=student_id,)
        .properties(width=700, height=450)
    ).interactive()
    return senti_lineplot


def question_senti_barplot(senti_df):
    """barplot for individual question's sentiment"""
    senti_plot = (
        alt.Chart(senti_df)
        .mark_bar()
        .encode(
            alt.Y("questions", title="Questions", sort="-x"),
            alt.X(cts.SENTI, title="Sentiment"),
            tooltip=[alt.Tooltip(cts.SENTI, title="Sentiment")],
            opacity=alt.value(0.7),
            color=alt.condition(
                alt.datum[cts.SENTI] > 0,
                alt.value("steelblue"),
                alt.value("red"),
            ),
        )
        .properties(width=700, height=450)
    ).interactive()

    return senti_plot


def doc_sim_heatmap(df_sim):
    """heatmap for document similarity between each student"""
    heatmap = (
        alt.Chart(df_sim)
        .mark_rect()
        .encode(
            x=alt.X("doc_1", sort=None, title="student"),
            y=alt.Y("doc_2", sort="-x", title="student"),
            color="similarity",
            tooltip=[alt.Tooltip("similarity", title="similarity")],
        )
        .properties(width=600, height=550)
    ).interactive()
    return heatmap


def tp_hist_plot(df_tp):
    """histogram plot for topics"""
    tp_hist = (
        alt.Chart(df_tp).mark_bar().encode(
            alt.X("Dominant_Topic:N"),
            y="count()",
            color=cts.ASSIGNMENT,
            tooltip=[
                alt.Tooltip("Student", title="Student"),
                alt.Tooltip("Topic_Keywords", title="Keywords")
            ],
            ).properties(height=600, width=700)
    ).interactive()
    return tp_hist


def tp_scatter_plot(df_lda):
    """scatter plot for lda"""
    lda = alt.Chart(df_lda).mark_point(size=100, filled=True).encode(
        x='x',
        y='y',
        shape='topic:N',
        color='topic_num:N',
    ).interactive()
    return lda
