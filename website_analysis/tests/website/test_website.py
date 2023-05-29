import pytest
from pathlib import Path

from website_analysis.src.website.site import Website

@pytest.fixture
def imagesSite():
    w = Website("website_analysis/tests/resources/cs417-one-lecture")
    yield w

@pytest.fixture
def cssSite():
    w = Website("website_analysis/tests/resources/cs-landing-page")
    yield w

class TestWebsite:
    def test_basePath(self, imagesSite, cssSite):
        blank = Website()
        assert blank.basePath == Path.cwd(), f"Blank Path is {blank.basePath}"

        assert imagesSite.basePath == Path.cwd() / "website_analysis/tests/resources/cs417-one-lecture", f"Image Path is {imagesSite.basePath}"
        assert cssSite.basePath == Path.cwd() / "website_analysis/tests/resources/cs-landing-page", f"CSS Path is {cssSite.basePath}"

    def test_htmlFiles(self, imagesSite, cssSite):
        assert len(imagesSite.htmlFiles) != 0, f"Base Path is {imagesSite.basePath}"

        for html in imagesSite.htmlFiles:
            assert html.endswith(".html"), f"Non-HTML file included"
