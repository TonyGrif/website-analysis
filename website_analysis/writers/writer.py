from datetime import date

class Writer:
    def __init__(self, fn=None):
        self.fileName = fn

    @property
    def fileName(self) -> str:
        return self._fileName
    
    @fileName.setter
    def fileName(self, fn) -> None:
        if fn is None:
            today = date.today()
            self._fileName = today.strftime("%Y-%m-%d") + "-summary"
        else:
            self._fileName = fn
    
