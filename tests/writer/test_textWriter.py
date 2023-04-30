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

    def test_write(self, tWriter):
        tWriter.write()
        assert tWriter.fullPath.parent.is_dir()
        assert tWriter.fullPath.is_file()
        Path.unlink(tWriter.fullPath)
        Path.rmdir(Path.cwd() / "output/")

        tWriter.fullPath = "build/output"
        assert not tWriter.fullPath.exists()
        tWriter.write()
        assert tWriter.fullPath.parent.is_dir()
        assert tWriter.fullPath.is_file()
        Path.unlink(tWriter.fullPath)
        Path.rmdir(Path.cwd() / "build")
