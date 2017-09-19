class Vertex:

    _error_hash = "Error".__hash__()

    def __init__(self, name="", initial=False, final=False, error=False):
        self._error = error
        if error:
            self._name = "Error"
            self._initial = False
            self._final = False
            return
        else:
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
        return Vertex(
            name=self.name + other.name,
            initial=self.initial & other.initial,
            final=self.final & other.final,
            error=self.error | other.error)

    def __or__(self, other):
        return Vertex(
            name=self.name + other.name,
            initial=self.initial | other.initial,
            final=self.final | other.final,
            error=self.error & other.error)


def initial(vertex):
    return vertex.initial


def final(vertex):
    return vertex.final


def error(vertex):
    return vertex.error
