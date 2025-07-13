from datetime import datetime

def current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
