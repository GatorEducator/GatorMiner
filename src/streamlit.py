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
        st.sidebar.success("To continue")
        st.title("Frequency Analysis")
        frequency()
    elif analysis_mode == "Sentiment Analysis":
        st.sidebar.success("To continue")
        st.title("Sentiment Analysis")


def frequency():
    df = pd.DataFrame(md.collect_md(directory))
    # st.write(az.dir_frequency(directory))
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
            alt.Y("word", title="words"),
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
