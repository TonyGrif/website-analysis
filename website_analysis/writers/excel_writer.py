from pathlib import Path 


class ExcelWriter:
    def __init__(self, full):
        self.fullPath = full

    def write(self):
        Path.mkdir(self.fullPath.parent, parents=True)
        Path.touch(self.fullPath)

    @property 
    def fullPath(self) -> Path:
        return self._fullPath

    @fullPath.setter
    def fullPath(self, value):
        self._fullPath = Path(value + ".xlsx").resolve()
