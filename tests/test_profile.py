# tests/test_profile.py

import pandas as pd
from dfflow.profile import profile_summary

def test_profile_summary():
    df = pd.DataFrame({
        'X': [1, None],
        'Y': [3, 4]
    })
    summary = profile_summary(df)
    assert 'shape' in summary
    assert 'columns' in summary
    assert 'null_counts' in summary
    assert summary['null_counts']['X'] == 1
