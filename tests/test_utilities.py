import pytest
from pathlib import Path
from os import getcwd

from src.utilities import findDirectory


@pytest.fixture
def directory():
    directory = Path(getcwd() + "/tests/resources/")
    yield directory


class TestUtilities:
    def test_findDirectory(self, directory):
        found = findDirectory(directory)
        assert found is True, f"{directory} not found"

        found = findDirectory(directory / "cs417-one-lecture")
        assert found is True, f"{directory} not found"

        found = findDirectory(directory / "330-landing-page")
        assert found is False, f"Unexpectedly found {directory}"

        found = findDirectory(directory / "cs-landing-page/index.html")
        assert found is False, f"Unexpectedly accepting files"

        found = findDirectory(Path(".."))
        assert found is True, f"Relative path not being accepted"

        found = findDirectory(Path("tests/../tests/writer/.."))
        assert found is True, f"Relative path navigation not working"
