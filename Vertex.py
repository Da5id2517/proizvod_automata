class Vertex:

    _error_hash = "Error".__hash__()

    def __init__(self, name="", initial=False, final=False, error=False):
        if error:
            self._name = "Error"
        else:
            self._name = name
        self._initial = initial
        self._final = final
        self._error = error

    @property
    def name(self):
        return self._name

    @property
    def initial(self):
        return self._initial

    @property
    def final(self):
        return self._final

    @property
    def error(self):
        return self._error

    def represent(self):
        pass

    # TODO: overload operators for vertex!
    def descartes_product(self, other, operator):
        return operator(self, other)

    def __repr__(self):
        return "{initial}{open}{self.name}{close}"\
            .format(self=self,
                    open="(" if self.final else "",
                    close=")" if self.final else "",
                    initial="->" if self.initial else "")

    def __hash__(self):
        if self.error:
            return self._error_hash
        else:
            return self.name.__hash__()

    def __eq__(self, other):
        return self.name == other.name \
               and self.initial == other.initial \
               and self.final == other.final \
               and self.error == other.error

    def __and__(self, other):
        if self.error or other.error:
            return self if self.error else other
        return Vertex(self.name + other.name,
                      self.initial & other.initial,
                      self.final & other.final)

    def __or__(self, other):
        if self.error and other.error:
            return self
        return Vertex(
            self.name + other.name,
            self.initial | other.initial,
            self.final | other.final)


def initial(vertex):
    return vertex.initial


def final(vertex):
    return vertex.final


def error(vertex):
    return vertex.error
