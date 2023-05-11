import pytest
from pathlib import Path

from website_analysis.writers.json_writer import JsonWriter
from website_analysis.website.site import Website


@pytest.fixture
def writer():
    j = JsonWriter("tests/output/test")
    yield j


class TestJsonWriter:
    def test_fullPath(self, writer):
        assert writer.fullPath == Path(Path.cwd() / "tests/output/test.json")

        writer.fullPath = "build/file"
        assert writer.fullPath == Path(Path.cwd() / "build/file.json")

    def test_write(self, writer):
        writer.write()
        assert writer.fullPath.parent.is_dir()
        assert writer.fullPath.is_file()
        Path.unlink(writer.fullPath)

        writer.fullPath = "tests/output/test2"
        writer.write()
        assert writer.fullPath.parent.is_dir()
        assert writer.fullPath.is_file()
        Path.unlink(writer.fullPath)
        Path.rmdir(Path.cwd() / "tests/output")
