from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Iterable

import git.exc
from git import Repo
from packaging.version import Version, parse

from .logger import logger


def run(test_command: str, paths: Iterable[Path], target_version: Version) -> bool:
    repo = get_repo()
    fetch_tags(repo)

    literal_latest_version = get_latest_version(repo)
    latest_version = parse(literal_latest_version)

    if target_version <= latest_version:
        logger.error("Target version should be greater than last version")
        return False

    chekcout_paths_from_reference(repo, literal_latest_version, paths)

    test_succeeded = run_test_command(test_command)

    discard_changes(repo)

    return is_breaking_change_expected(target_version, latest_version, test_succeeded)


def is_breaking_change_expected(
    target_version: Version, latest_version: Version, test_succeeded: bool
) -> bool:
    major_increased = target_version.major > latest_version.major
    return major_increased or test_succeeded


def get_repo(path: Path = Path()) -> Repo:
    try:
        return Repo(path)
    except git.exc.InvalidGitRepositoryError as exception:
        error_message = "repo not found"
        raise ValueError(error_message) from exception


def run_test_command(test_command: str) -> bool:
    command = test_command.split(" ")
    logger.info("Running command %s", command)
    completed_proccess = subprocess.run(command)
    return completed_proccess.returncode == 0


def fetch_tags(repo: Repo) -> None:
    logger.info("Fetching Tags")
    for remote in repo.remotes:
        fetch_info = remote.fetch(tags=True)
        for info in fetch_info:
            logger.info("Successfully fetched %s at %s", info.ref, info.commit)


def get_latest_version(repo: Repo) -> str:
    logger.info("Get latest Tag")
    latest_tag: str = repo.git.describe(abbrev=0, tags=True)
    return latest_tag


def chekcout_paths_from_reference(
    repo: Repo, reference: str, paths: Iterable[Path]
) -> None:
    """Using checkout in sparse mode to bring only one path from reference"""
    for path in paths:
        logger.info("Get %s from %s", path, reference)
        repo.git.checkout(reference, "--", path)


def discard_changes(repo: Repo) -> None:
    logger.info("Discard Changes")
    repo.git.reset("HEAD")
    repo.git.checkout(".")
