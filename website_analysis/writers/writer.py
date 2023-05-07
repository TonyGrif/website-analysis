from datetime import date

from .text_writer import TextWriter
from .json_writer import JsonWriter
from .excel_writer import ExcelWriter 
from ..website.website import Website


class WriteManager:
    def __init__(self, od=None, fn=None):
        self.outputDirectory = od
        self.fileName = fn
        self._tWrite = TextWriter(self.outputDirectory + "/" + self.fileName)
        self._jWrite = JsonWriter(self.outputDirectory + "/" + self.fileName)
        self._eWrite = ExcelWriter(self.outputDirectory + "/" + self.fileName)

    def write(self):
        self._tWrite.write()
        self._jWrite.write()
        self._eWrite.write() 

    @property
    def outputDirectory(self) -> str:
        return self._outputDirectory

    @outputDirectory.setter
    def outputDirectory(self, od) -> None:
        if od is None:
            self._outputDirectory = "output"
        else:
            self._outputDirectory = od

    @property
    def fileName(self) -> str:
        return self._fileName

    @fileName.setter
    def fileName(self, fn) -> None:
        if fn is None:
            today = date.today()
            self._fileName = today.strftime("%Y-%m-%d") + "-summary"
        else:
            self._fileName = fn
