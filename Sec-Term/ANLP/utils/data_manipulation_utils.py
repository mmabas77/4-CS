def apply_minmax_scaling(minmax_scaling, original_data):
    """
    You want to scale data when you're using methods based on measures of how far apart data points are,
     like support vector machines (SVM) or k-nearest neighbors (KNN).
    :param minmax_scaling: Import it using
     'from mlxtend.preprocessing import minmax_scaling'
    :param original_data: Numpy one-dimensional array
    :return: Numpy one-dimensional array
    """
    return minmax_scaling(original_data, columns=[0])



def apply_normalization(stats, original_data):
    """
    In general, you'll normalize your data if you're going to be
     using a machine learning or statistics technique that assumes your data
      is normally distributed. Some examples of these include
       linear discriminant analysis (LDA) and Gaussian naive Bayes.
        --
        Pro tip
        any method with "Gaussian" in the name probably assumes normality.
        --
    :param stats: Import it using
    'from scipy import stats'
    :param original_data: Numpy one-dimensional array
    :return: Numpy one-dimensional array
    """
    return stats.boxcox(original_data)


def replace_matches_in_column(fuzzywuzzy, df, column, string_to_match, min_ratio=90):
    """
    Function to replace rows in the provided column of the provided dataframe
    that match the provided string above the provided ratio with the provided string
    :param fuzzywuzzy: fuzzywuzzy package import it using
    'import fuzzywuzzy'
    :param df: Dataframe Object
    :param column: Column to match against
    :param string_to_match: String to match against
    :param min_ratio: Min matching ratio to replace (Default : 90)
    :return: Dataframe Object
    """

    # get a list of unique strings
    strings = df[column].unique()

    # get the top 10 closest matches to our input string
    matches = fuzzywuzzy.process.extract(
        string_to_match,
        strings,
        limit=10,
        scorer=fuzzywuzzy.fuzz.token_sort_ratio
    )

    # only get matches with a ratio > min_ratio
    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]

    # get the rows of all the close matches in our dataframe
    rows_with_matches = df[column].isin(close_matches)

    # replace all rows with close matches with the input matches
    df.loc[rows_with_matches, column] = string_to_match

    return df
