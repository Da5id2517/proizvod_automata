class Vertex:
    def __init__(self, name, initial=False, final=False):
        self._name = name
        self._initial = initial
        self._final = final

    @property
    def name(self):
        return self._name

    @property
    def initial(self):
        return self._initial

    @property
    def final(self):
        return self._final

    def descartes_product(self, other_vertex):
        if (self._name == 404) or (other_vertex.get_name() == 404):
            return Vertex(404)
        return Vertex([self._name, other_vertex.get_name()], self._initial & other_vertex.get_initial(), \
                    self._final & other_vertex.get_final())

    def __str__(self):
        return "{initial}{final}{self.name}"\
            .format(self=self,
                    initial="I" if self.initial else "",
                    final="F" if self.final else "")

    def __eq__(self, other):
        return self.name == other.name \
               and self.initial == other.initial \
               and self.final == other.final

    def __hash__(self):
        if type(self._name) is list:
            return sum(self._name)*17
        return self._name