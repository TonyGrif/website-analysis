import pytest
from pathlib import Path
from os import getcwd

from utils import find_directory


@pytest.fixture
def directory():
    yield Path(getcwd())


class TestUtils:
    def test_find_directory(self, directory):
        assert find_directory(directory) is True
        assert find_directory(directory / "src") is True

        with pytest.raises(FileNotFoundError) as fnfe:
            find_directory(directory / "source")
            assert type(fnfe.value.__cause__) is FileNotFoundError

        with pytest.raises(NotADirectoryError) as nde:
            find_directory(directory / "main.py")
            assert type(nde.value.__cause__) is NotADirectoryError

        assert find_directory(directory / "..") is True
