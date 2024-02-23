
import pandas as pd

def df_sampler(df:pd.DataFrame, sample_type, sample_size):
    if sample_type == 'head':
        return df.head(sample_size)
    elif sample_type == 'tail':
        return df.tail(sample_size)
    elif sample_type == 'random':
        return df.sample(sample_size)
    else:
        raise ValueError('Invalid sample size, please enter a number smaller than the dataframe size.')