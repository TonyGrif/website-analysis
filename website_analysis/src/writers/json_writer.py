from pathlib import Path
import json

from ..website.site import Website

class JsonWriter:
    '''
    Maintains and operates the JSON file. 

    Attributes:
        website (Website): The website whos data will be written to the JSON file.
        fullPath (Path): The full path to the JSON file.
    '''
    def __init__(self, site, full):
        '''
        Constructor for the JsonWriter class. 

        Parameters:
            site (Website): The website whos data will be written to the JSON file. 
            full (Path): The path of the JSON file.
        '''
        self._website = site
        self.fullPath = full

    def write(self):
        '''
        Function to write all necessary data to the JSON file.
        '''
        Path.mkdir(self.fullPath.parent, parents=True, exist_ok=True)
        Path.touch(self.fullPath)

        json_string = {"basePath" : str(self._website.basePath)}

        with open(self.fullPath, "w") as file:
            json.dump(json_string, file)


    @property
    def fullPath(self) -> Path:
        return self._fullPath

    @fullPath.setter
    def fullPath(self, value):
        self._fullPath = Path(value + ".json").resolve()
