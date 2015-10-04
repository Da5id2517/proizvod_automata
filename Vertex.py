class Vertex:
    def __init__(self, name, initial=False, final=False):
        self._name = name
        self._initial = initial
        self._final = final

    def get_name(self):
        return self._name

    def get_initial(self):
        return self._initial

    def get_final(self):
        return self._final

    def set_final(self):
        self._final = True

    def set_initial(self):
        self._initial = True

    def descartes_product(self, other_vertex):
        if (self._name == 404) or (other_vertex.get_name() == 404):
            return Vertex(404)
        return Vertex([self._name, other_vertex.get_name()], self._initial & other_vertex.get_initial(), \
                    self._final & other_vertex.get_final())

    def __repr__(self):
        return "{:s}".format(str(self._name))

    def __eq__(self, other):
        return self._name == other.get_name()

    def __hash__(self):
        if type(self._name) is list:
            return sum(self._name)*17
        return self._name