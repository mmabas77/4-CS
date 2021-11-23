def multi_csv_contact_to_dataframe(pd, *paths):
    """
    Read multi csv files and convert them into single dataframe using concat function.
    :param pd: Pandas package
    :param paths: String paths to csv file
    :return: Data Frame Object
    """
    arr = []
    for path in paths:
        arr.append(csv_to_dataframe(pd, path))
    return pd.concat(arr)


def csv_to_dataframe(pd, path, index=None):
    """
    Read csv file and convert to dataframe.
    :param pd: Pandas package
    :param path: String path to csv file
    :param index: Index of col to use for indexing
    :return: Data Frame Object
    """
    if index is not None:
        return pd.read_csv(path, index_col=index)
    return pd.read_csv(path)


def print_dataframe_essential_info(df, np):
    """
    Prints some essential information of the dataframe.
    :param df: Data Frame Object
    :param np: Numpy package
    """
    missing_values_count = df.isnull().sum()
    # how many total missing values do we have?
    total_cells = np.product(df.shape)
    total_missing = missing_values_count.sum()
    # percent of data that is missing
    percent_missing = (total_missing / total_cells) * 100

    # Shape
    print('Data frame shape: {0}'.format(df.shape))
    # Info
    print('Data frame info: {0}'.format(df.info()))
    # Correlation
    print('\n---Data Correlation ---\n{0}'.format(df.corr()))
    # Null counter
    print('\n---Data frame null count ---\n{0}'.format(missing_values_count))
    print('\nTotal values : {0}\nTotal missing values : {1}\nRemaining : {2}'
          .format(total_cells, total_missing, total_cells - total_missing))
    print('\nRemaining percentage : {0}%\nMissing percentage : {1}%'
          .format(100. - percent_missing, percent_missing))
    print('---')


def print_dataframe_exploration_info(df):
    """
    Prints some exploration information of the dataframe.
    :param df: Data Frame Object
    """
    # Shape
    print('Data frame shape: {0}'.format(df.shape))
    # Header
    print('\n---Data frame header ---\n{0}'.format(df.head()))
    print('---')
    # Description
    print('\n---Data frame description ---\n{0}'.format(df.describe()))
    print('---')
    # Data Types
    print('\n---Data frame data types ---\n{0}'.format(df.dtypes))
    print('---')


def print_dataframe_additional_info(df):
    """
    Prints additional information of the dataframe.
    :param df: Data Frame Object
    """
    cols = df.columns
    for col in cols:
        print('\n---Column {0} Unique Values---\n{1}'
              .format(col, df[col].unique()))
        print('---')
        print('\n---Column {0} Value Counts---\n{1}'
              .format(col, df[col].value_counts()))
        print('---')
        print('\n---Column {0} Value Counts---\n{1}'
              .format(col, df[col].value_counts()))
        print('---')
        print('\n---Column {0} Null Values---\n{1}'
              .format(col, df[col].loc[df[col].isnull()]))
        print('---')


def drop_rows_with_null(df):
    """
    Drops all rows with null value.
    :param df: Data Frame Object
    :return: Data Frame Object
    """
    return df.dropna()


def drop_cols_with_null(df):
    """
    Drops all columns with null value.
    :param df: Data Frame Object
    :return: Data Frame Object
    """
    return df.dropna(axis=1)


def drop_cols_with_names(df, *col_names):
    """
    Drops many columns with specified names.
    :param df: Data Frame Object
    :param col_names: Names of columns to drop
    :return: Data Frame Object
    """
    for col_name in col_names:
        df = drop_col_with_name(df, col_name)
    return df


def drop_col_with_name(df, col_name):
    """
    Drops a column with specified name.
    :param df: Data Frame Object
    :param col_name: Name of column to drop
    :return: Data Frame Object
    """
    return df.drop(col_name, 1)
