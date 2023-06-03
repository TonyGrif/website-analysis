import pytest
from pathlib import Path

from website_analysis.src.writers.text_writer import TextWriter
from website_analysis.src.website.site import Website

@pytest.fixture 
def site():
    site = Website("website_analysis/tests/resources/cs-landing-page")
    yield site

@pytest.fixture
def tWriter(site):
    tWriter = TextWriter(site, "website_analysis/tests/output/text")
    yield tWriter


class TestTextWriter:
    def test_write(self, tWriter):
        tWriter.write()
        assert tWriter.fullPath.parent.exists(), f"Directory path not created"
        assert tWriter.fullPath.parent.is_dir(), f"Expected directory, found file"
        assert tWriter.fullPath.exists(), f"File not created"
        assert tWriter.fullPath.is_file(), f"Expected file, found directory"

        file = open(tWriter.fullPath, "r")
        for lines in file:
            temp = '\t'.join(tWriter._website.htmlFiles)
            assert lines in temp

        Path.unlink(tWriter.fullPath)

        tWriter.fullPath = "website_analysis/tests/output/test2"
        tWriter.write()
        assert tWriter.fullPath.parent.exists(), f"Directory path not created"
        assert tWriter.fullPath.parent.is_dir(), f"Expected directory, found file"
        assert tWriter.fullPath.exists(), f"File not created"
        assert tWriter.fullPath.is_file(), f"Expected file, found directory"
        Path.unlink(tWriter.fullPath)
        Path.rmdir(Path.cwd() / "website_analysis/tests/output")

    def test_file(self, tWriter):
        assert tWriter.fullPath == Path(Path.cwd() / "website_analysis/tests/output/text.txt"), f"Full path is {tWriter.fullPath}"

        tWriter.fullPath = "build/output"
        assert tWriter.fullPath == Path(Path.cwd() / "build/output.txt"), f"Full path is {tWriter.fullPath}"
