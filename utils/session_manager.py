class SessionManager:
    def __init__(self) -> None:
        self.sessions = {}

    def add_session(self, name: str, value: object) -> None:
        self.sessions[name] = value
