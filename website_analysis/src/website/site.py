from pathlib import Path

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
        else:
            self._basePath = (Path.cwd() / path).resolve()
