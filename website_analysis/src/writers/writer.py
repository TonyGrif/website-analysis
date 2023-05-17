from datetime import date

from .text_writer import TextWriter
from .json_writer import JsonWriter
from .excel_writer import ExcelWriter 
from ..website.site import Website


class WriteManager:
    """
    Maintains and operates all available file writers.

    Attributes:
        outputDirectory (str): The output directory to write all files to.
        fileName (str): The name that all output files will be.
        tWrite (TextWriter): The text writer.
        jWrite (JsonWriter): The JSON writer.
        eWrite (ExcelWriter): The excel writer.
    """

    def __init__(self, site, od=None, fn=None):
        """
        Constructor for the WriteManager class.

        Parameters:
            od (str): The output directory to write all files to.
            fn (str): The name that all output files will be.
        """
        self.outputDirectory = od
        self.fileName = fn
        self._tWrite = TextWriter(self.outputDirectory + "/" + self.fileName)
        self._jWrite = JsonWriter(site, self.outputDirectory + "/" + self.fileName)
        self._eWrite = ExcelWriter(self.outputDirectory + "/" + self.fileName)

    def write(self):
        """
        Function to write to all available files.
        """
        self._tWrite.write()
        self._jWrite.write()
        self._eWrite.write()

    @property
    def outputDirectory(self) -> str:
        """
        Return the output directory.

        Return:
            outputDirectory (str): The currently set output directory.
        """
        return self._outputDirectory

    @outputDirectory.setter
    def outputDirectory(self, od) -> None:
        """
        Set the output directory.

        Sets the output directory based on the input. If the input is None,
        set the directory to ./output/

        Parameters:
            od (str): Determines the output directory.
        """
        if od is None:
            self._outputDirectory = "output"
        else:
            self._outputDirectory = od

    @property
    def fileName(self) -> str:
        """
        Return the current file name.

        Return:
            fileName (str): The currently set file name.
        """
        return self._fileName

    @fileName.setter
    def fileName(self, fn) -> None:
        """
        Set the standard file name.

        Sets the current file name based on the input. If the input is None,
        sets the file name to today's date in the following format: YEAR-MONTH-DAY-summary.EXTENSION

        Parameters:
            fn (str): Determines the file name.
        """
        if fn is None:
            today = date.today()
            self._fileName = today.strftime("%Y-%m-%d") + "-summary"
        else:
            self._fileName = fn
