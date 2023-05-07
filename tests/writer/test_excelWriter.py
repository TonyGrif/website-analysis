import pytest
from pathlib import Path  

from website_analysis.writers.excel_writer import ExcelWriter 


@pytest.fixture
def writer():
    e = ExcelWriter("tests/output/test")
    yield e 


class TestExcelWriter:
    def test_fullPath(self, writer):
        assert writer.fullPath == Path.cwd() / "tests/output/test.xlsx"
        
        writer.fullPath = "build/exlFile"
        assert writer.fullPath == Path.cwd() / "build/exlFile.xlsx"

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
