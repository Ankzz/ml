import pandas as pd
import numpy as np

from pytest import fixture

from data_processing import  clean_df

@fixture
def sample_df():
    age_list = [10 + np.random.randint(4) * 10 for _ in range(4)]
    age_list.append(None)
    return pd.DataFrame({
        "user_id": np.random.randint(5),
        "age": age_list,
        "score": 15 + np.random.randint(5)
    })

def test_case_1(sample_df):
    df = clean_df(sample_df)
    assert(len(df["age"])==4)
