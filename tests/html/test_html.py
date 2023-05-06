import pytest
from pathlib import Path

from website_analysis.html.html import Html

@pytest.fixture
def imagesHtml():
    h = Html("tests/resources/cs417-one-lecture")
    yield h

@pytest.fixture
def cssHtml():
    h = Html("tests/resources/cs-landing-page")
    yield h 

class TestHtml:
    def test_basePath(self, imagesHtml, cssHtml):
        assert imagesHtml.basePath == Path.cwd() / "tests/resources/cs417-one-lecture"
        assert cssHtml.basePath == Path.cwd() / "tests/resources/cs-landing-page"
