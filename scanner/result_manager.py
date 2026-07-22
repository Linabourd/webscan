class ResultManager:
    def __init__(self) -> None:
        self.results = []

    def add_result(self, result: dict) -> None:
        self.results.append(result)
