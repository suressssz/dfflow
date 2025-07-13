# tests/test_flow.py

import pandas as pd
from dfflow import DFLogger, FlowPipeline, drop_nulls, lowercase_columns

def test_flow_pipeline(tmp_path):
    log_file = tmp_path / "flow_log.txt"
    logger = DFLogger(log_file=str(log_file), mode='text')

    df = pd.DataFrame({
        'Name': ['Tom', None],
        'Age': [25, 22]
    })

    pipe = FlowPipeline(logger=logger)
    pipe.add_step("Drop Nulls", drop_nulls)
    pipe.add_step("Lowercase Columns", lowercase_columns)

    result = pipe.run(df)

    # Check nulls dropped
    assert result.isnull().sum().sum() == 0
    # Check columns lowercased
    for col in result.columns:
        assert col.islower()

    # Check log created
    with open(log_file) as f:
        content = f.read()
        assert "Drop Nulls" in content
