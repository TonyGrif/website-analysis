from bs4 import BeautifulSoup

from pathlib import Path

class Html:
    def __init__(self, p):
        self.imageCollection = []

        self.path = p

    def _parse(self):        
        with open(self.path) as path:
            soup = BeautifulSoup(path, "html.parser")

        self.imageCollection = soup.findAll("img")

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, set):
        if set.endswith(".html") and Path(set).exists():
            self._path = Path.cwd() / set

            # Clear previous runs
            self.imageCollection.clear()
            self._parse()
        else:
            return
