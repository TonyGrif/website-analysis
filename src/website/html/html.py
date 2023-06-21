from bs4 import BeautifulSoup

from pathlib import Path

class Html:
    def __init__(self, p):
        self.path = p

    def _parse(self):
        return

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, set):
        if set.endswith(".html"):
            self._path = Path.cwd() / set 
        else:
            return
