from pathlib import Path

class Website:
    def __init__(self, path=None):
        self.basePath = path
        self.htmlFiles = self._htmlFileFinder()

    @property 
    def basePath(self) ->  Path:
        return self._basePath

    @basePath.setter
    def basePath(self, path) -> None:
        if path is None:
            self._basePath = Path.cwd()
        else:
            self._basePath = (Path.cwd() / path).resolve()

    def _htmlFileFinder(self) -> list:
        pList = []
        for path in Path(self.basePath).rglob("*.html"):
            pList.append(str(path))

        return pList
