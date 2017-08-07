class Edge:
    def __init__(self, start, end, letter=""):
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

    def represent(self):
        pass

    # We are beside ourselves.
    def __repr__(self):
        return "{self.start} -> {self.letter} -> {self.end}".format(self=self)

    def __hash__(self):
        return self.start.__hash__() \
               + self.end.__hash__() \
               + self.letter.__hash__()

    def __eq__(self, other):
        return self.start == other.start \
               and self.end == other.end \
               and self.letter == other.letter
