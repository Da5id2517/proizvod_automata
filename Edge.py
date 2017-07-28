class Edge:
    def __init__(self, start, end, letter=" "):
        self._start = start
        self._end = end
        self._letter = letter

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def letter(self):
        return self._letter

    def __str__(self):
        return "{self.start} -> {self.letter} -> {self.end}".format(self=self)
