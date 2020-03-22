import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

import analyzer as az
import markdown as md

directory = "resources/test"


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


def frequency():
    freq_type = st.sidebar.selectbox(
        "Type of frequency analysis", ["Overall", "Individual"]
    )
    if freq_type == "Overall":
        st.sidebar.success(
            'To continue see individual frequency analysis select "Individual"'
        )
        overall_freq()
    elif freq_type == "Individual":
        individual_freq()


def overall_freq():
    freq_amount = st.sidebar.slider(
        "Select a range of Most frequent words?", 0, 50, value=25
    )
    freq_df = pd.DataFrame(
        az.dir_frequency(directory, freq_amount), columns=["word", "freq"]
    )
    st.write(freq_df)

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


def individual_freq():
    df = pd.DataFrame(md.collect_md(directory))
    st.write(df)
    students = st.multiselect(
        label="Enter the names of specific students below:", options=df["Reflection by"]
    )


if __name__ == "__main__":
    main()
