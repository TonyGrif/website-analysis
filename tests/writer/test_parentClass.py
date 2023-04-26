import pytest
from datetime import date

from website_analysis.writers.writer import Writer

@pytest.fixture()
def writer():
    writer = Writer()
    yield writer

@pytest.fixture()
def nonDefWriter():
    writer = Writer("build", "file-output")
    yield writer

class TestWriter:
    def test_outputDirectory(self, writer, nonDefWriter):
        assert writer.outputDirectory == "output"

        assert nonDefWriter.outputDirectory == "build"

    def test_fileName(self, writer, nonDefWriter):
        today = date.today()
        assert writer.fileName == today.strftime("%Y-%m-%d") + "-summary"

        assert nonDefWriter.fileName == "file-output"