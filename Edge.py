from Vertex import Vertex
#begin i end moraju da ti budu vertexi, hence the decorator is required!

class Edge:
    def __init__(self, start, end, letter=" "):
        self._start = start
        self._end = end
        self._letter = letter

    def get_start(self):
        return self._start

    def get_end(self):
        return self._end

    def get_letter(self):
        return self._letter