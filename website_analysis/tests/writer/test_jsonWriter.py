import pytest
from pathlib import Path

from website_analysis.src.writers.json_writer import JsonWriter
from website_analysis.src.website.site import Website

@pytest.fixture()
def site():
    site = Website(Path.cwd() / "tests/resources/cs417-one-lecture")
    yield site

@pytest.fixture
def writer(site):
    j = JsonWriter(site, "tests/output/test")
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
