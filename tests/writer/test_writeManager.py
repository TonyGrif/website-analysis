import pytest
from datetime import date

from website_analysis.writers.writer import WriteManager

@pytest.fixture()
def writer():
    writer = WriteManager()
    yield writer

@pytest.fixture()
def nonDefWriter():
    writer = WriteManager("build", "file-output")
    yield writer

class TestWriter:
    def test_outputDirectory(self, writer, nonDefWriter):
        assert writer.outputDirectory == "output"

        assert nonDefWriter.outputDirectory == "build"

    def test_fileName(self, writer, nonDefWriter):
        today = date.today()
        assert writer.fileName == today.strftime("%Y-%m-%d") + "-summary"

        assert nonDefWriter.fileName == "file-output"
