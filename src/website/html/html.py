class Html:
    def __init__(self, p):
        self.path = p

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, set):
        self._path = set 
