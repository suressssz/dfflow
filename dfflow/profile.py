def profile_summary(df):
    return {
        "shape": df.shape,
        "columns": list(df.columns),
        "null_counts": df.isnull().sum().to_dict()
    }
