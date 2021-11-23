import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder


def ordinal_encoder(df, trans_list=None):
    if trans_list is None:
        trans_list = df.select_dtypes(include=["object"]).columns
    encoder = OrdinalEncoder()
    encoder.fit(df[trans_list])
    df[trans_list] = encoder.transform(df[trans_list])
    return df


def standard_scaler(df, trans_list=None, exception_list=None):
    if trans_list is None:
        trans_list = df.select_dtypes(include=[np.number]).columns
    if exception_list is not None:
        trans_list = [item for item in trans_list if item not in exception_list]
    scaler = StandardScaler()
    scaler.fit(df[trans_list])
    df[trans_list] = scaler.transform(df[trans_list])
    return df
