from git import Repo
import pytest


@pytest.fixture
def temp_git_dir(tmpdir):
    git_dir = tmpdir.join('gits')
    Repo.init(git_dir)
    yield git_dir
