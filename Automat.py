from Vertex import Vertex
from Edge import Edge


class Automaton:
    def __init__(self, vertices, edges, alphabet=[]):
        self._vertices = vertices
        self._edges = edges
        self._alphabet = alphabet

    def get_alphabet(self):
        return self._alphabet

    def get_initial(self):
        for k in self._vertices:
            if k.get_initial() is True:
                return k

    def get_final(self):
        for k in self._vertices:
            if k.get_final() is True:
                return k

    def get_vertices(self):
        return self._vertices

    def get_edges(self):
        return self._edges

    def add_vertex(self, vertex):
        if vertex in self._vertices:
            self._vertices.remove(vertex)
        self._vertices.append(vertex)

    def add_edge(self, edge):
        self._edges.append(edge)
        if edge.get_letter() not in self._alphabet:
            self._alphabet.append(edge.get_letter())

    def add_letter_to_alphabet(self, letter):
        self._alphabet.append(letter)

    def transition_by_letter(self, current_vertex, letter):
        for k in self._edges:
            if (k.get_start() == current_vertex) & (k.get_letter() == letter):
                return k.get_end()
        return None

    def accepts_word(self, word):
        current_vertex = self.get_initial()
        for l in list(word):
            current_vertex = self.transition_by_letter(current_vertex, l)
        return current_vertex.get_final()

    def complete(self):
        l = Vertex(404)
        self.add_vertex(l)
        for k in self._vertices:
            for letter in self._alphabet:
                if self.transition_by_letter(k, letter) is None:
                    self.add_edge(Edge(k, l, letter))

    def multiply_automaton(self, other_automaton):
        if set(self._alphabet) != set(other_automaton.get_alphabet()):
            raise Exception("Alphabets of automatons must match!")
        all_states = set([])
        all_edges = set([])
        self.complete()
        other_automaton.complete()
        for k in self._vertices:
            for j in other_automaton.get_vertices():
                for letter in self._alphabet:
                    new1 = k.descartes_product(j)
                    new2 = self.transition_by_letter(k, letter).descartes_product(other_automaton.transition_by_letter(j, letter))
                    new_e = Edge(new1, new2, letter)
                    all_edges.add(new_e)
                    all_states.add(new1)
                    all_states.add(new2)
        return Automaton(all_states, all_edges, self._alphabet)