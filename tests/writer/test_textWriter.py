import pytest
from pathlib import Path

from src.writers.text_writer import TextWriter
from src.website.site import Website

@pytest.fixture 
def site():
    site = Website("tests/resources/")
    yield site

@pytest.fixture
def tWriter(site):
    tWriter = TextWriter(site, "tests/output/text/text1")
    yield tWriter


class TestTextWriter:
    def test_write(self, tWriter):
        tWriter.write()
        assert tWriter.fullPath.parent.exists(), f"Directory path not created"
        assert tWriter.fullPath.parent.is_dir(), f"Expected directory, found file"
        assert tWriter.fullPath.exists(), f"File not created"
        assert tWriter.fullPath.is_file(), f"Expected file, found directory"

        temp = []
        for path in tWriter._website.htmlFiles:
            temp.append(path.path)

        file = open(tWriter.fullPath, "r")
        for lines in file:
            line = lines.strip("\n")
            assert line in str(temp), f"Incorrect file added"

        Path.unlink(tWriter.fullPath)

        tWriter.fullPath = "tests/output/text/text2"
        tWriter.write()
        assert tWriter.fullPath.parent.exists(), f"Directory path not created"
        assert tWriter.fullPath.parent.is_dir(), f"Expected directory, found file"
        assert tWriter.fullPath.exists(), f"File not created"
        assert tWriter.fullPath.is_file(), f"Expected file, found directory"
        Path.unlink(tWriter.fullPath)
        Path.rmdir(Path.cwd() / "tests/output/text")

    def test_file(self, tWriter):
        assert tWriter.fullPath == Path(Path.cwd() / "tests/output/text/text1.txt"), f"Full path is {tWriter.fullPath}"

        tWriter.fullPath = "tests/build/output"
        assert tWriter.fullPath == Path(Path.cwd() / "tests/build/output.txt"), f"Full path is {tWriter.fullPath}"
