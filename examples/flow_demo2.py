import pandas as pd
from dfflow import DFLogger, FlowPipeline
from dfflow.cleaning import drop_nulls, lowercase_columns
from dfflow.profile import profile_summary

# Create a sample DataFrame
data = {
    "Name": ["Suresh", None, "Sunil", "Shiva", "Linga"],
    "Age": [23, 26, 23, 24, None]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n")

# Setup the DFLogger
logger = DFLogger(
    log_file='dfflow_log2.txt',  # Log file path
    mode='text'                          # 'text' or 'json'
)

# Create the FlowPipeline
pipe = FlowPipeline(logger=logger)

# Add cleaning steps
pipe.add_step("Drop Nulls", drop_nulls)
pipe.add_step("Lowercase Columns", lowercase_columns)

# Run the pipeline
result_df = pipe.run(df)

print("Final Cleaned DataFrame:")
print(result_df)
print("\n")

# Profile Summary
summary = profile_summary(result_df)
print("Profile Summary:")
print(summary)
