import pytest
import json
from pathlib import Path

from src.writers.json_writer import JsonWriter
from src.website.site import Website

@pytest.fixture()
def site():
    site = Website(Path.cwd() / "tests/resources/cs417-one-lecture")
    yield site

@pytest.fixture
def writer(site):
    j = JsonWriter(site, "tests/output/JSON")
    yield j

class TestJsonWriter:
    def test_fullPath(self, writer):
        assert writer.fullPath == Path(Path.cwd() / "tests/output/JSON.json"), f"Full path is {writer.fullPath}"

        writer.fullPath = "build/file"
        assert writer.fullPath == Path(Path.cwd() / "build/file.json"), f"Full path is {writer.fullPath}"

    def test_write(self, writer):
        writer.write()
        assert writer.fullPath.parent.exists(), f"Directory path not created"
        assert writer.fullPath.parent.is_dir(), f"Expected directory, found file"
        assert writer.fullPath.exists(), f"File not created"
        assert writer.fullPath.is_file(), f"Expected file, found directory"

        # Testing the contents of file
        json_info = json.load(open(writer.fullPath))
        
        assert json_info['basePath'] == (str(Path.cwd() / "tests/resources/cs417-one-lecture"))
        assert len(json_info['pages']) >= 1

        Path.unlink(writer.fullPath)

        writer.fullPath = "tests/output/test2"
        writer.write()
        assert writer.fullPath.parent.exists(), f"Directory path not created"
        assert writer.fullPath.parent.is_dir(), f"Expected directory, found file"
        assert writer.fullPath.exists(), f"File not created"
        assert writer.fullPath.is_file(), f"Expected file, found directory"
        Path.unlink(writer.fullPath)
        Path.rmdir(Path.cwd() / "tests/output")
