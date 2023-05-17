from pathlib import Path
import json

from ..website.site import Website

class JsonWriter:
    def __init__(self, site, full):
        self._website = site
        self.fullPath = full

    def write(self):
        Path.mkdir(self.fullPath.parent, parents=True, exist_ok=True)
        Path.touch(self.fullPath)



    @property
    def fullPath(self) -> Path:
        return self._fullPath

    @fullPath.setter
    def fullPath(self, value):
        self._fullPath = Path(value + ".json").resolve()
