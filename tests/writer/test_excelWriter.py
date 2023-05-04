import pytest
from pathlib import Path  

from website_analysis.writers.excel_writer import ExcelWriter 


@pytest.fixture
def writer():
    e = ExcelWriter("output/test")
    yield e 


class TestExcelWriter:
    def test_fullPath(self, writer):
        assert writer.fullPath == Path.cwd() / "output/test.xlsx"
        
        writer.fullPath = "build/exlFile"
        assert writer.fullPath == Path.cwd() / "build/exlFile.xlsx"

    def test_write(self, writer):
        assert False
