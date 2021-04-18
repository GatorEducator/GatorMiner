# import pandas as pd
# import src.visualization as vis
#
#
# def basic_frame():
#     """A basic dataframe with no frills"""
#     return pd.DataFrame()
#
# def importpanda(import_data):
#     raw_df = pd.DataFrame()
#     for item in import_data:
#         single_df = pd.DataFrame(item)
#         raw_df = pd.concat([raw_df, single_df]).fillna("")
#     tidy_df = df_preprocess(raw_df)
#     return tidy_df, raw_df
