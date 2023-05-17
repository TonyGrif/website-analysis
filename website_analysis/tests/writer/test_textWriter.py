import pytest
from pathlib import Path

from website_analysis.src.writers.text_writer import TextWriter


@pytest.fixture
def tWriter():
    tWriter = TextWriter("tests/output/test")
    yield tWriter


class TestTextWriter:
    def test_file(self, tWriter):
        assert tWriter.fullPath == Path(Path.cwd() / "tests/output/test.txt")

        tWriter.fullPath = "build/output"
        assert tWriter.fullPath == Path(Path.cwd() / "build/output.txt")

    def test_write(self, tWriter):
        tWriter.write()
        assert tWriter.fullPath.parent.is_dir()
        assert tWriter.fullPath.is_file()
        Path.unlink(tWriter.fullPath)

        tWriter.fullPath = "tests/output/test2"
        tWriter.write()
        assert tWriter.fullPath.parent.is_dir()
        assert tWriter.fullPath.is_file()
        Path.unlink(tWriter.fullPath)
        Path.rmdir(Path.cwd() / "tests/output")
