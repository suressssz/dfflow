import pandas as pd
from dfflow import DFLogger, FlowPipeline, drop_nulls
import os
log_path = os.path.join(os.path.dirname(__file__), 'dfflow_log.txt')
logger = DFLogger(log_file=log_path, mode='text')


logger = DFLogger()
pipe = FlowPipeline(logger=logger)

pipe.add_step("Drop Nulls", drop_nulls)

df = pd.DataFrame({
    'name': ['Suresh', None, 'Jerry', 'Sunil', 'Linga'],
    'age': [23, 26, None, 23, 24]
})

pipe.run(df)
