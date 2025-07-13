from .decorators import log_step

@log_step("Drop Nulls")
def drop_nulls(df):
    return df.dropna()

@log_step("Lowercase Columns")
def lowercase_columns(df):
    df.columns = [col.lower() for col in df.columns]
    return df
