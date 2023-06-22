from pathlib import Path

from .html.html import Html

class Website:
    def __init__(self, path=None):
        self.basePath = path

    @property 
    def basePath(self) ->  Path:
        return self._basePath

    @basePath.setter
    def basePath(self, path) -> None:
        if path is None:
            self._basePath = Path.cwd()
            self.htmlFiles = self._htmlFileFinder()
        else:
            self._basePath = (Path.cwd() / path).resolve()
            self.htmlFiles = self._htmlFileFinder()

    def _htmlFileFinder(self) -> list:
        pList = []
        for path in Path(self.basePath).rglob("*.html"):
            pList.append(Html(str(path)))

        return pList
