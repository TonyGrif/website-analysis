import pytest
from pathlib import Path

from src.website.html.html import Html

@pytest.fixture
def html():
    h = Html("tests/resources/cs417-one-lecture/index.html")
    yield h

class TestHtml:
    def test_path(self, html):
        # Test initial setter
        assert html.path == Path.cwd() / "tests/resources/cs417-one-lecture/index.html", f"Path is {html.path}"

        # Not html file
        html.path = "tests/resources/cs417-one-lecture/integralDI1.png"
        assert html.path != "tests/resources/cs417-one-lecture/integralDI1.png", f"Path is {html.path}"

        # Non existent file
        html.path = "tests/resources/cs-landing-page/examAnswers.html"
        assert html.path != "tests/resources/cs-landing-page/examAnswers.html"