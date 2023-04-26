import pytest
from datetime import date

from website_analysis.writers.writer import Writer

@pytest.fixture()
def writer():
    writer = Writer()
    yield writer

@pytest.fixture()
def nonDefWriter():
    writer = Writer("file-output")
    yield writer

class TestWriter:
    def test_fileName(self, writer, nonDefWriter):
        # Test default name
        today = date.today()
        assert writer.fileName == today.strftime("%Y-%m-%d") + "-summary"

        # Test non-default name
        assert nonDefWriter.fileName == "file-output"