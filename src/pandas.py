import pandas as pd
import src.visualization as vis


def basic_frame():
    """A basic dataframe with no frills"""
    return pd.DataFrame()

def importpanda(import_data):
    raw_df = pd.DataFrame()
    for item in import_data:
        single_df = pd.DataFrame(item)
        raw_df = pd.concat([raw_df, single_df]).fillna("")
    tidy_df = df_preprocess(raw_df)
    return tidy_df, raw_df

def df_preprocess(df):
    """build and preprocess (combine, normalize, tokenize) text"""
    # filter out first two columns -- non-report content
    cols = df.columns[2:]
    # combining text into combined column
    df["combined"] = df[cols].apply(
        lambda row: "\n".join(row.values.astype(str)), axis=1
    )
    # normalize
    df[cts.NORMAL] = df["combined"].apply(lambda row: az.normalize(row))
    # tokenize
    df[cts.TOKEN] = df[cts.NORMAL].apply(lambda row: az.tokenize(row))
    return df