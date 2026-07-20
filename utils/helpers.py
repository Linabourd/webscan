def ensure_directory(path: str) -> None:
    import os

    os.makedirs(path, exist_ok=True)
