from pathlib import Path


class TextWriter:
    """
    Responsible for creating and writing information to a text file.

    Attributes:
        fullPath (Path): A path for the text file to be writting to.
    """

    def __init__(self, full):
        """
        Constructor for the text writer.

        Parameters:
            full (str): String representation of the location of the text file.
        """
        self.fullPath = full

    def write(self):
        """
        Responsible for the creation of the text file.

        This function will create the directories and the file if necessary.
        """
        Path.mkdir(self.fullPath.parent, parents=True, exist_ok=True)
        Path.touch(self.fullPath)

    @property
    def fullPath(self) -> Path:
        """
        Return the current full path to the text file.

        Return:
            fullPath (Path): The full path to the text file.
        """
        return self._fullPath

    @fullPath.setter
    def fullPath(self, full):
        """
        Set the current full path to the text file.

        Parameters:
            full (str): Value to set the full path to.
        """
        self._fullPath = Path(full + ".txt").resolve()
