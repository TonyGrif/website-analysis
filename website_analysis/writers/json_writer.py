from pathlib import Path

class JsonWriter:
    def __init__(self, full):
        self.fullPath = full

    @property
    def fullPath(self) -> Path:
        return self._fullPath


    @fullPath.setter
    def fullPath(self, value):
        self._fullPath = Path(value + ".json").resolve()
