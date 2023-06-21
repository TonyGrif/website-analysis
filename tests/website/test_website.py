import pytest
from pathlib import Path

from src.website.site import Website

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
        resourceLoc = "tests/resources"

        blank = Website()
        assert blank.basePath == Path.cwd(), f"Blank Path is {blank.basePath}"

        assert imagesSite.basePath == Path.cwd() / resourceLoc / "cs417-one-lecture", f"Image Path is {imagesSite.basePath}"
        assert cssSite.basePath == Path.cwd() / resourceLoc / "cs-landing-page", f"CSS Path is {cssSite.basePath}"

        imagesSite.basePath = resourceLoc
        assert imagesSite.basePath == Path.cwd() / resourceLoc, f"New base path it {imagesSite.basePath}"

    def test_htmlFiles(self, imagesSite, cssSite):
        resourceLoc = "tests/resources"

        assert len(imagesSite.htmlFiles) == 1, f"Base Path is {imagesSite.basePath}"

        for html in imagesSite.htmlFiles:
            assert str(html.path).endswith(".html"), f"Non-HTML file included"

        cssSite.basePath = resourceLoc
        assert len(cssSite.htmlFiles) == 2, f"Counted {len(cssSite.htmlFiles)}"
