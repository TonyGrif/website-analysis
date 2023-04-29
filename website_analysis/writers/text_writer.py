from pathlib import Path 

class TextWriter:
    def __init__(self, full):
        self.fullPath = full 

    def write(self):
        pass

        
    @property 
    def fullPath(self) -> Path:
        return self._fullPath

    @fullPath.setter
    def fullPath(self, full):
        self._fullPath = Path(full + ".txt").resolve()
