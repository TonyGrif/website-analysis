import pytest
from pathlib import Path

from website_analysis.website.site import Website

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
        blank = Website()
        assert blank.basePath == Path.cwd(), f"Blank Path is {blank.basePath}"

        assert imagesSite.basePath == Path.cwd() / "tests/resources/cs417-one-lecture", f"Image Path is {imagesSite.basePath}"
        assert cssSite.basePath == Path.cwd() / "tests/resources/cs-landing-page", f"CSS Path is {cssSite.basePath}"
