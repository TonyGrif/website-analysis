import pytest
from pathlib import Path

from website_analysis.html.website import Website

@pytest.fixture
def imagesSite():
    w = Website("tests/resources/cs417-one-lecture")
    yield w

@pytest.fixture
def cssSite():
    w = Website("tests/resources/cs-landing-page")
    yield w

class TestWebsite:
    def test_basePath(self, imagesSite, cssSite):
        assert imagesSite.basePath == Path.cwd() / "tests/resources/cs417-one-lecture"
        assert cssSite.basePath == Path.cwd() / "tests/resources/cs-landing-page"
