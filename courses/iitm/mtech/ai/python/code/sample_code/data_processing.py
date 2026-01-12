
import pandas as pd

def clean_df(df:pd.DataFrame, col: str= "age", threshold: int=1):
    df = df[df[col]>threshold]
    return df
