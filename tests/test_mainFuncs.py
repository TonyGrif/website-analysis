import pytest
from pathlib import Path
from os import getcwd

from website_analysis.main import findDirectory

@pytest.fixture
def directory():
    directory = Path(getcwd() + "/tests/resources/")
    yield directory

class TestMain:
    def test_findDirectory(self, directory):
        found = findDirectory(directory)
        assert found == True

        found = findDirectory(directory / "cs417-one-lecture")
        assert found == True

        found = findDirectory(directory / "330-landing-page")
        assert found == False

        found = findDirectory(directory / "cs-landing-page/index.html")
        assert found == False
