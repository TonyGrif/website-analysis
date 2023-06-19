import pytest
from pathlib import Path  

from src.writers.excel_writer import ExcelWriter 


@pytest.fixture
def writer():
    e = ExcelWriter("tests/output/excel")
    yield e 


class TestExcelWriter:
    def test_fullPath(self, writer):
        assert writer.fullPath == Path.cwd() / "tests/output/excel.xlsx"
        
        writer.fullPath = "build/exlFile"
        assert writer.fullPath == Path.cwd() / "build/exlFile.xlsx"

    def test_write(self, writer):
        writer.write()
        assert writer.fullPath.parent.exists(), f"Directory path not created"
        assert writer.fullPath.parent.is_dir(), f"Expected directory, found file"
        assert writer.fullPath.exists(), f"File not created"
        assert writer.fullPath.is_file(), f"Expected file, found directory"
        Path.unlink(writer.fullPath)

        writer.fullPath = "tests/output/test2"
        writer.write()
        assert writer.fullPath.parent.exists(), f"Directory path not created"
        assert writer.fullPath.parent.is_dir(), f"Expected directory, found file"
        assert writer.fullPath.exists(), f"File not created"
        assert writer.fullPath.is_file(), f"Expected file, found directory"
        Path.unlink(writer.fullPath)
        Path.rmdir(Path.cwd() / "tests/output")
