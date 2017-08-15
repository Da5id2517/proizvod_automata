import sys
import operator

from Vertex import Vertex, initial
from Edge import Edge


class Automaton:
    def __init__(self, vertices=set(), edges=set(), alphabet=set("")):
        self._vertices = vertices
        self._edges = edges
        self._alphabet = alphabet
        self.complete()
        self.clean_up()

    @property
    def alphabet(self):
        return self._alphabet

    @property
    def vertices(self):
        return self._vertices

    @property
    def error(self):
        for vertex in self.vertices:
            if vertex.error:
                return vertex

    @property
    def edges(self):
        return self._edges

    def fetch(self, mod):
        for vertex in self.vertices:
            if mod(vertex):
                return vertex
            else:
                return self.error

    def represent(self):
        pass

    def transition_by_letter(self, current_vertex, letter):
        if letter not in self.alphabet:
            return self.error

        for edge in self.edges:
            if edge.start == current_vertex and edge.letter == letter:
                return edge.end if edge.end in self.vertices else self.error

        return self.error

    def accepts_word(self, word):
        current_vertex = self.fetch(initial)
        for letter in word:
            current_vertex = self.transition_by_letter(current_vertex, letter)
        return current_vertex.final if not current_vertex.error\
            else False

    # NOTE: you complete the automaton upon creation.
    def complete(self):
        error_state = Vertex("Error", initial=False, final=False, error=True)
        self.vertices.add(error_state)
        for vertex in self.vertices:
            for letter in self.alphabet:
                if vertex.error:
                    if self.transition_by_letter(vertex, letter) == self.error:
                        self.edges.add(Edge(vertex, error_state, letter))

    def clean_up(self):
        for edge in self.edges.copy():
            if edge.start.error:
                self.edges.remove(edge)

    def multiply_automaton(self, other, operator):
        # Nice error handling...
        if self.alphabet != other.alphabet:
            print("Alphabets must match!\n")
            sys.exit(0)
        vertices = set()
        edges = set()
        for vertex_1 in self.vertices:
            for vertex_2 in other.vertices:
                for letter in self.alphabet:

                    new_vertex_1 = vertex_1.descartes_product(vertex_2,
                                                              operator)
                    new_vertex_2 = self.transition_by_letter(
                        vertex_1, letter).descartes_product(
                        other.transition_by_letter(vertex_2, letter), operator)

                    new_edge = Edge(new_vertex_1, new_vertex_2, letter)

                    edges.add(new_edge)
                    vertices.add(new_vertex_1)
                    vertices.add(new_vertex_2)

        return Automaton(vertices, edges, self.alphabet)

    def __and__(self, other):
        return self.multiply_automaton(other, operator.__and__)

    def __or__(self, other):
        return self.multiply_automaton(other, operator.__or__)
