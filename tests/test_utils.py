import pytest
from pathlib import Path
from os import getcwd

from utils import *


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

    def test_create_report_directory(self, directory):
        if not Path(Path.cwd() / "reports").exists():
            create_report_directory()
            assert Path(directory / "reports").exists()

            Path.rmdir(Path.cwd() / "reports")

        create_report_directory(directory / "tests/reports")
        assert Path(directory / "tests/reports").exists()

        create_report_directory(directory / "tests/reports")
        assert Path(directory / "tests/reports").exists()

        Path.rmdir(directory / "tests/reports")

        create_report_directory(directory / "tests/parent/report")
        assert Path(directory / "tests/parent/report").exists()

        Path.rmdir(directory / "tests/parent/report")
        Path.rmdir(directory / "tests/parent/")
