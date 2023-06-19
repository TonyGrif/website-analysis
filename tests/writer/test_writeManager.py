import pytest
from datetime import date
from pathlib import Path

from src.writers.writer import WriteManager
from src.website.site import Website

@pytest.fixture()
def site():
    site = Website(Path.cwd() / "tests/resources/cs417-one-lecture")
    yield site

@pytest.fixture()
def writer(site):
    writer = WriteManager(site, "tests/output")
    yield writer

@pytest.fixture()
def nonDefWriter(site):
    writer = WriteManager(site, "tests/build", "file-output")
    yield writer

class TestWriter:
    def test_write(self, writer, nonDefWriter):
        writer.write()
        assert Path(
            writer.outputDirectory
        ).exists(), f"{writer.outputDirectory} not created."
        assert Path(
            writer.outputDirectory
        ).is_dir(), f"{writer.outputDirectory} not created as directory."

        pathNoExtension = writer.outputDirectory + "/" + writer.fileName
        assert Path(pathNoExtension + ".txt").exists(), f"Text file not created."
        assert Path(
            pathNoExtension + ".txt"
        ).is_file(), f"Expected text file, found directory."

        assert Path(pathNoExtension + ".json").exists(), f"JSON file not created."
        assert Path(
            pathNoExtension + ".json"
        ).is_file(), f"Expected JSON file, found directory."

        assert Path(pathNoExtension + ".xlsx").exists(), f"Excel file not created."
        assert Path(
            pathNoExtension + ".xlsx"
        ).is_file(), f"Expected excel file, found directory."

        # Remove files and directory created
        Path.unlink(Path(pathNoExtension + ".txt").resolve())
        Path.unlink(Path(pathNoExtension + ".json").resolve())
        Path.unlink(Path(pathNoExtension + ".xlsx").resolve())
        Path.rmdir(Path(writer.outputDirectory).resolve())

        nonDefWriter.write()
        assert Path(
            nonDefWriter.outputDirectory
        ).exists(), f"{nonDefWriter.outputDirectory} not created."
        assert Path(
            nonDefWriter.outputDirectory
        ).is_dir(), f"{nonDefWriter.outputDirectory} not created as directory."

        pathNoExtension = nonDefWriter.outputDirectory + "/" + nonDefWriter.fileName
        assert Path(pathNoExtension + ".txt").exists(), f"Text file not created."
        assert Path(
            pathNoExtension + ".txt"
        ).is_file(), f"Expected text file, found directory."

        assert Path(pathNoExtension + ".json").exists(), f"JSON file not created."
        assert Path(
            pathNoExtension + ".json"
        ).is_file(), f"Expected JSON file, found directory."

        assert Path(pathNoExtension + ".xlsx").exists(), f"Excel file not created."
        assert Path(
            pathNoExtension + ".xlsx"
        ).is_file(), f"Expected excel file, found directory."

        # Remove files and directory created
        Path.unlink(Path(pathNoExtension + ".txt").resolve())
        Path.unlink(Path(pathNoExtension + ".json").resolve())
        Path.unlink(Path(pathNoExtension + ".xlsx").resolve())
        Path.rmdir(Path(nonDefWriter.outputDirectory).resolve())

    def test_outputDirectory(self, site, writer, nonDefWriter):
        defWrite = WriteManager(site)
        assert defWrite.outputDirectory == "output", f"Default initialization error"

        assert writer.outputDirectory == "tests/output", f"Initialization error."

        writer.outputDirectory = "newDirectory"
        assert writer.outputDirectory == "newDirectory", f"Setter error."
        today = date.today()
        assert (
            writer.fileName == today.strftime("%Y-%m-%d") + "-summary"
        ), f"Unexpectedly changing file name"

        assert nonDefWriter.outputDirectory == "tests/build", f"Initialization error."

        nonDefWriter.outputDirectory = "output"
        assert nonDefWriter.outputDirectory == "output", f"Setter error."
        assert (
            nonDefWriter.fileName == "file-output"
        ), f"Unexpectedly changing file name."

    def test_fileName(self, writer, nonDefWriter):
        today = date.today()
        assert (
            writer.fileName == today.strftime("%Y-%m-%d") + "-summary"
        ), f"Initialization error."

        writer.fileName = "landingPage-summary"
        assert writer.fileName == "landingPage-summary", f"Setter error."
        assert (
            writer.outputDirectory == "tests/output"
        ), f"Unexpectedly changing output directory."

        assert nonDefWriter.fileName == "file-output", f"Initialization error."

        nonDefWriter.fileName = "417-summary"
        assert nonDefWriter.fileName == "417-summary", f"Setter error."
        assert (
            nonDefWriter.outputDirectory == "tests/build"
        ), f"Unexpectedly changing output directory"
