from pathlib import Path


class TextWriter:
    def __init__(self, full):
        self.fullPath = full

    def write(self):
        Path.mkdir(self.fullPath.parent, parents=True, exist_ok=True)
        Path.touch(self.fullPath)

    @property
    def fullPath(self) -> Path:
        return self._fullPath

    @fullPath.setter
    def fullPath(self, full):
        self._fullPath = Path(full + ".txt").resolve()
