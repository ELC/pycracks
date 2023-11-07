from pathlib import Path
from typing import Generator
from pycracks.pycracks import get_repo

import tempfile

import pytest

from git import Repo


@pytest.fixture
def folder() -> Generator[Path, None, None]:
    with tempfile.TemporaryDirectory() as directory_name:
        yield Path(directory_name)


@pytest.fixture
def folder_with_repo(folder: Path) -> Path:
    Repo.init(folder)
    return folder


def test_get_repo_without_repo(folder: Path) -> None:
    with pytest.raises(ValueError, match="repo not found"):
        get_repo(folder)


def test_get_repo_with_repo(folder_with_repo: Path) -> None:
    get_repo(folder_with_repo)
