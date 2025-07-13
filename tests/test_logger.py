# tests/test_logger.py

import pandas as pd
import os
from dfflow.logger import DFLogger

def test_text_logging(tmp_path):
    log_file = tmp_path / "test_log.txt"
    logger = DFLogger(log_file=str(log_file), mode='text')
    df = pd.DataFrame({'A': [1, 2]})
    logger.log("Test log message", df)

    assert log_file.exists()
    with open(log_file) as f:
        content = f.read()
        assert "Test log message" in content
        assert "A" in content

def test_json_logging(tmp_path):
    log_file = tmp_path / "test_log.json"
    logger = DFLogger(log_file=str(log_file), mode='json')
    df = pd.DataFrame({'B': [3, 4]})
    logger.log("JSON log message", df)

    assert log_file.exists()
    with open(log_file) as f:
        content = f.read()
        assert "JSON log message" in content
