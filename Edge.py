from Vertex import Vertex


class Edge:
    def __init__(self, start, end, letter=""):
        if isinstance(start, Vertex) and isinstance(end, Vertex):
            self._start = start
            self._end = end
            self._letter = letter
        else:
            raise ValueError("Start and end must be of type Vertex.")

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
        if self.start == self.end:
            return "\t{start} edge [loop above] node {letter} ()\n".format(
                start="(" + self.start.name + ")",
                letter="{" + self.letter + "}"
            )
        return "\t{start} edge node {letter} {end}\n".format(
            start="(" + self.start.name + ")",
            letter="{" + self.letter + "}",
            end="(" + self.end.name + ")"
        )

    def __repr__(self):
        return "{self.start} --> {self.letter} --> {self.end}".format(self=self)

    def __hash__(self):
        return self.start.__hash__() \
               + self.end.__hash__() \
               + self.letter.__hash__()

    def __eq__(self, other):
        return self.start == other.start \
               and self.end == other.end \
               and self.letter == other.letter
