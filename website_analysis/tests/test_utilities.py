import pytest
from pathlib import Path
from os import getcwd

from website_analysis.src.utilities import findDirectory


@pytest.fixture
def directory():
    directory = Path(getcwd() + "/tests/resources/")
    yield directory


class TestUtilities:
    def test_findDirectory(self, directory):
        found = findDirectory(directory)
        assert found is True

        found = findDirectory(directory / "cs417-one-lecture")
        assert found is True

        found = findDirectory(directory / "330-landing-page")
        assert found is False

        found = findDirectory(directory / "cs-landing-page/index.html")
        assert found is False

        found = findDirectory(Path(".."))
        assert found is True

        found = findDirectory(Path("tests/../tests/writer/.."))
        assert found is True
