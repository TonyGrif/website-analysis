import pytest
from pathlib import Path

from website_analysis.writers.text_writer import TextWriter

@pytest.fixture
def tWriter():
    tWriter = TextWriter("output/test")
    yield tWriter
    
class TestTextWriter:
    def test_file(self, tWriter):
        assert tWriter.fullPath == Path(Path.cwd() / "output/test.txt")

        tWriter.fullPath = "build/output"
        assert tWriter.fullPath == Path(Path.cwd() / "build/output.txt")
