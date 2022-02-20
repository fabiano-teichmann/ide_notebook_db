import os
from typing import List

from git import Repo


def list_changed_files() -> List[str]:
    repo = Repo()
    files = []
    for item in repo.index.diff(None):
        if os.path.isfile(item.a_path):
            if item.a_path.endswith(".py"):
                files.append(item.a_path)
        else:
            raise FileNotFoundError(f"Not found file {item.a_path}")
    return files
