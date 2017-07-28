from Vertex import Vertex, initial, final
from Edge import Edge


class Automaton:
    def __init__(self, vertices=[], edges=[], alphabet=""):
        self._vertices = vertices
        self._edges = edges
        self._alphabet = alphabet
        self.complete()

    @property
    def alphabet(self):
        return self._alphabet

    @property
    def vertices(self):
        return self._vertices

    @property
    def error(self):
        for vertex in self.vertices:
            if vertex.name == "Error":
                return vertex

    @property
    def edges(self):
        return self._edges

    def fetch(self, mod):
        for vertex in self.vertices:
            if mod(vertex):
                return vertex

    def transition_by_letter(self, current_vertex, letter):
        for edge in self.edges:
            if edge.start == current_vertex and edge.letter == letter:
                return edge.end if edge.end in self.vertices else self.error
            # TODO: change this to the appropriate error state.
        return self.error

    def accepts_word(self, word):
        current_vertex = self.fetch(initial)
        for letter in word:
            current_vertex = self.transition_by_letter(current_vertex, letter)
        return current_vertex.final

    # NOTE: you complete the automaton upon creation.
    def complete(self):
        error_state = Vertex("Error", initial=False, final=False)
        for vertex in self.vertices:
            for letter in self.alphabet:
                if self.transition_by_letter(vertex, letter) is None:
                    self.edges.append(Edge(vertex, error_state, letter))

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
    #                 new2 = self.
    #   transition_by_letter(k, letter).descartes_product(
    #                   other_automaton.transition_by_letter(j, letter))
    #                 new_e = Edge(new1, new2, letter)
    #                 all_edges.add(new_e)
    #                 all_states.add(new1)
    #                 all_states.add(new2)
    #     return Automaton(all_states, all_edges, self._alphabet)
