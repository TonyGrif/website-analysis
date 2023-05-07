from pathlib import Path

class Website:
    def __init__(self, path):
        self.basePath = path

    @property 
    def basePath(self):
        return self._basePath

    @basePath.setter
    def basePath(self, value):
        self._basePath = (Path.cwd() / value).resolve()
