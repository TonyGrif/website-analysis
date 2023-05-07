import pytest
from datetime import date
from pathlib import Path

from website_analysis.writers.writer import WriteManager
from website_analysis.website.website import Website

@pytest.fixture()
def writer():
    writer = WriteManager()
    yield writer


@pytest.fixture()
def nonDefWriter():
    writer = WriteManager("build", "file-output")
    yield writer


class TestWriter:
    def test_write(self, writer, nonDefWriter):
        writer.write()
        assert Path(writer.outputDirectory).is_dir()
        assert Path(writer.outputDirectory + "/" + writer.fileName + ".txt").is_file()
        assert Path(writer.outputDirectory + "/" + writer.fileName + ".json").is_file()
        assert Path(writer.outputDirectory + "/" + writer.fileName + ".xlsx").is_file()

        Path.unlink(
            Path(writer.outputDirectory + "/" + writer.fileName + ".txt").resolve()
        )
        Path.unlink(
            Path(writer.outputDirectory + "/" + writer.fileName + ".json").resolve()
        )
        Path.unlink(
            Path(writer.outputDirectory + "/" + writer.fileName + ".xlsx").resolve()
        )
        Path.rmdir(Path(writer.outputDirectory).resolve())

        nonDefWriter.write()
        assert Path(nonDefWriter.outputDirectory).is_dir()
        assert Path(
            nonDefWriter.outputDirectory + "/" + nonDefWriter.fileName + ".txt"
        ).is_file()
        assert Path(nonDefWriter.outputDirectory + "/" + nonDefWriter.fileName + ".json").is_file()
        assert Path(nonDefWriter.outputDirectory + "/" + nonDefWriter.fileName + ".xlsx").is_file()

        Path.unlink(
            Path(
                nonDefWriter.outputDirectory + "/" + nonDefWriter.fileName + ".txt"
            ).resolve()
        )
        Path.unlink(
            Path(nonDefWriter.outputDirectory + "/" + nonDefWriter.fileName + ".json").resolve()
        )
        Path.unlink(
            Path(nonDefWriter.outputDirectory + "/" + nonDefWriter.fileName + ".xlsx").resolve()
        )
        Path.rmdir(Path(nonDefWriter.outputDirectory).resolve())

    def test_outputDirectory(self, writer, nonDefWriter):
        assert writer.outputDirectory == "output"

        assert nonDefWriter.outputDirectory == "build"

    def test_fileName(self, writer, nonDefWriter):
        today = date.today()
        assert writer.fileName == today.strftime("%Y-%m-%d") + "-summary"

        assert nonDefWriter.fileName == "file-output"
