# ----- ----- Importing Section ----- ----- #
# Data libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import fuzzywuzzy
from sklearn import preprocessing
# ML Libraries
from sklearn.model_selection import train_test_split
# ->Lazy Predictor
from lazypredict.Supervised import LazyClassifier
from lazypredict.Supervised import LazyRegressor

# My utils
from distributed.profile import plot_data

from utils import df_utils
from utils import data_manipulation_utils
from utils import plt_utils

from utils import nlp_utils


# ----- ----- ----- END ----- ----- ----- #


def prepare_data_frame():
    # Read data
    df = read_data()
    # Explore & Plot - 1
    explore_and_plot_df(df)
    # Enhance
    df = enhance(df)
    # Explore & Plot - 2
    explore_and_plot_df(df)
    # Return
    return df


def read_data():
    true_df = df_utils.csv_to_dataframe(pd, './dataset/True.csv')
    true_df["c"] = 1
    false_df = df_utils.csv_to_dataframe(pd, './dataset/Fake.csv')
    false_df["c"] = 0
    df = pd.concat([true_df, false_df])
    df = df.sample(frac=1)
    df.reset_index(inplace=True)
    df.drop(["index"], axis=1, inplace=True)

    # Todo : Remove this in production code
    df = df[:100]
    return df


def enhance(df):
    df = df_utils.drop_cols_with_names(df, 'title', 'subject', 'date')
    df = df_utils.drop_rows_with_null(df)
    # Corpus calculations as text
    process_df_text(df)
    return df


def process_df_text(df):
    # Lowercase
    df['text'] = df['text'].str.lower()

    # Stopwords
    df['stopwords'] = df.apply(
        lambda row: nlp_utils.count_stopwords(row['text']),
        axis=1
    )
    df['text'] = df.apply(
        lambda row: nlp_utils.remove_stopwords(row['text']),
        axis=1
    )

    # Punctuations
    df['punctuations'] = df.apply(
        lambda row: nlp_utils.count_punctuation(row['text']),
        axis=1
    )
    df['text'] = df.apply(
        lambda row: nlp_utils.remove_punctuation(row['text']),
        axis=1
    )

    # Stem
    df['text_stem'] = df.apply(
        lambda row: nlp_utils.porter_stemmer(row['text']),
        axis=1
    )

    # Lem
    df['text_lem'] = df.apply(
        lambda row: nlp_utils.word_net_lemmatizer(row['text']),
        axis=1
    )

    print(df.head())
    pass


def explore_and_plot_df(df):
    df_utils.print_dataframe_essential_info(df, np)
    pass


def train_model(df):
    pass


def save_model(model):
    pass


def make_predictions(model):
    pass


def main():
    nlp_utils.download_book()
    df = prepare_data_frame()
    model = train_model(df)
    save_model(model)
    make_predictions(model)


if __name__ == "__main__":
    main()
