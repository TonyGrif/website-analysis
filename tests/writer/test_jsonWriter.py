import pytest
from pathlib import Path

from website_analysis.writers.json_writer import JsonWriter 

@pytest.fixture
def writer():
    j = JsonWriter("output/test")
    yield j

class TestJsonWriter:
    def test_fullPath(self, writer):
        assert writer.fullPath == Path(Path.cwd() / "output/test.json")

        writer.fullPath = "build/file"
        assert writer.fullPath == Path(Path.cwd() / "build/file.json")
