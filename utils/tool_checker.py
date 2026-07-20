import shutil


def is_tool_available(tool: str) -> bool:
    return shutil.which(tool) is not None
