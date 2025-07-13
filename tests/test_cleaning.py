# tests/test_cleaning.py

import pandas as pd
from dfflow.cleaning import drop_nulls, lowercase_columns

def test_drop_nulls():
    df = pd.DataFrame({
        'A': [1, None, 3],
        'B': [4, 5, None]
    })
    result = drop_nulls(df)
    assert result.isnull().sum().sum() == 0

def test_lowercase_columns():
    df = pd.DataFrame({
        'FirstName': [1, 2],
        'AGE': [3, 4]
    })
    result = lowercase_columns(df)
    for col in result.columns:
        assert col.islower()
