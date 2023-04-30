import pytest
from pathlib import Path
from os import getcwd

from website_analysis.utilities import findDirectory

@pytest.fixture
def directory():
    directory = Path(getcwd() + "/tests/resources/")
    yield directory

class TestUtilities:
    def test_findDirectory(self, directory):
        found = findDirectory(directory)
        assert found == True

        found = findDirectory(directory / "cs417-one-lecture")
        assert found == True

        found = findDirectory(directory / "330-landing-page")
        assert found == False

        found = findDirectory(directory / "cs-landing-page/index.html")
        assert found == False

        found = findDirectory(Path(".."))
        assert found == True

        found = findDirectory(Path("tests/../tests/writer/.."))
        assert found == True
