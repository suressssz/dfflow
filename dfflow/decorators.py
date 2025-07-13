def log_step(step_name):
    def decorator(func):
        def wrapper(df, *args, **kwargs):
            result = func(df, *args, **kwargs)
            print(f"[dfflow] Step: {step_name} completed.")
            return result
        return wrapper
    return decorator
