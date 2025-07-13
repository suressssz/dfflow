import datetime
import json

class DFLogger:
    def __init__(self, log_file='dfflow_log.txt', mode='text'):
        self.log_file = log_file
        self.mode = mode

    def log(self, message, df, level="INFO"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if self.mode == 'json':
            self._log_json(timestamp, message, df, level)
        else:
            self._log_text(timestamp, message, df, level)

    def _log_text(self, timestamp, message, df, level):
        with open(self.log_file, 'a') as f:
            f.write("="*50 + "\n")
            f.write(f"Timestamp : {timestamp}\n")
            f.write(f"Level     : {level}\n")
            f.write(f"Message   : {message}\n")
            f.write("DataFrame :\n")
            f.write(df.to_string())
            f.write("\n\n")

    def _log_json(self, timestamp, message, df, level):
        log_entry = {
            "timestamp": timestamp,
            "level": level,
            "message": message,
            "dataframe": df.to_dict(orient="records")
        }
        with open(self.log_file, 'a') as f:
            f.write(json.dumps(log_entry) + "\n")