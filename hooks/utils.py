from git import Repo
from typing import (
    Optional,
    Sequence,
    List,
)
import argparse


def get_untracked_files() -> List[str]:
    return Repo().untracked_files


def get_current_branch() -> str:
    return Repo().active_branch.name


class Runner:

    def __init__(self, argv: Optional[Sequence[str]] = None):
        self.parser = argparse.ArgumentParser()
        self.argv = argv

    def check(self):
        # Fail by default
        return 1
