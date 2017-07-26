from Vertex import Vertex
from Edge import Edge


class Automaton:
    def __init__(self, vertices=[], edges=[], alphabet=[]):
        self._vertices = vertices
        self._edges = edges
        self._alphabet = alphabet

    @property
    def alphabet(self):
        return self._alphabet

    @property
    def vertices(self):
        return self._vertices

    @property
    def edges(self):
        return self._edges

    # TODO: find a way to make the inital/final thing dynamic.
    @property
    def fetch_initial(self):
        for vertex in self.vertices:
            if vertex.initial:
                return vertex

    @property
    def fetch_final(self):
        for vertex in self.vertices:
            if vertex.final:
                return vertex

    # TODO: check if this is actually useful.
    # def add_vertex(self, vertex):
    #     if vertex in self._vertices:
    #         self._vertices.remove(vertex)
    #     self._vertices.append(vertex)
    #
    # def add_edge(self, edge):
    #     self._edges.append(edge)
    #     if edge.get_letter() not in self._alphabet:
    #         self._alphabet.append(edge.get_letter())
    #
    # def add_letter_to_alphabet(self, letter):
    #     self._alphabet.append(letter)

    def transition_by_letter(self, current_vertex, letter):
        for edge in self.edges:
            if edge.start == current_vertex and edge.letter == letter:
                return edge.end
            # TODO: change this to the appropriate error state.
        return None

    def accepts_word(self, word):
        current_vertex = self.fetch_initial
        for letter in word:
            current_vertex = self.transition_by_letter(current_vertex, letter)
        return current_vertex.final

    # TODO: Make the automaton complete and integrate this in __init__.
    # def complete(self):
    #     l = Vertex(404)
    #     self.add_vertex(l)
    #     for k in self._vertices:
    #         for letter in self._alphabet:
    #             if self.transition_by_letter(k, letter) is None:
    #                 self.add_edge(Edge(k, l, letter))

    # TODO: Read theory before rewriting this.
    # def multiply_automaton(self, other_automaton):
    #     if set(self._alphabet) != set(other_automaton.get_alphabet()):
    #         raise Exception("Alphabets of automatons must match!")
    #     all_states = set([])
    #     all_edges = set([])
    #     self.complete()
    #     other_automaton.complete()
    #     for k in self._vertices:
    #         for j in other_automaton.get_vertices():
    #             for letter in self._alphabet:
    #                 new1 = k.descartes_product(j)
    #                 new2 = self.transition_by_letter(k, letter).descartes_product(other_automaton.transition_by_letter(j, letter))
    #                 new_e = Edge(new1, new2, letter)
    #                 all_edges.add(new_e)
    #                 all_states.add(new1)
    #                 all_states.add(new2)
    #     return Automaton(all_states, all_edges, self._alphabet)