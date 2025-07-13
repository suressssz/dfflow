class FlowPipeline:
    def __init__(self, logger=None):
        self.steps = []
        self.logger = logger

    def add_step(self, name, func):
        self.steps.append((name, func))

    def run(self, df):
        for name, func in self.steps:
            df = func(df)
            if self.logger:
                self.logger.log(f"Step: {name}", df)
        return df
