from pathlib import Path

from website.site import Website


class TextWriter:
    """
    Responsible for creating and writing information to a text file.

    Attributes:
        website (Website): The website whos data will be written to the text file.
        fullPath (Path): A path for the text file to be writting to.
    """

    def __init__(self, site: Website, full: str):
        """
        Constructor for the text writer.

        Parameters:
            site (Website): The website whos data will be written to the text file.
            full (str): String representation of the location of the text file.
        """
        self._website = site
        self.fullPath = full

    def write(self):
        """
        Responsible for the creation of the text file.

        This function will create the directories and the file if necessary.
        """
        Path.mkdir(self.fullPath.parent, parents=True, exist_ok=True)
        Path.touch(self.fullPath)

        with open(self.fullPath, "w") as file:
            for pages in self._website.htmlFiles:
                page = Path(pages.path)
                page = page.relative_to(self._website.basePath)
                file.write(str(page))
                file.write("\n")

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
