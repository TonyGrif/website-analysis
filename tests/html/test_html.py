import pytest
from pathlib import Path

from website_analysis.html.html import Html

@pytest.fixture
def html():
    h = Html("tests/resources/cs-landing-page")
    yield h

class TestHtml:
    def test_basePath(self, html):
        assert html.basePath == Path.cwd() / "tests/resources/cs-landing-page"
