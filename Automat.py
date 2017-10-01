import operator
from re import compile, search
from math import log

from Vertex import Vertex, initial
from Edge import Edge


class Automaton:
    def __init__(self, vertices=set(), edges=set(), alphabet=set("")):
        vertices.add(Vertex(initial=False, final=False, error=True))
        self._vertices = vertices
        self._edges = edges
        self._alphabet = alphabet
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

    def _remove_vertex(self, vertex):
        vertices = self.vertices.copy()
        if isinstance(vertex, list):
            for v in vertex:
                vertices.remove(v)
            return vertices
        vertices.remove(vertex)
        return vertices

    def fetch(self, mod):
        for vertex in self.vertices:
            if mod(vertex):
                return vertex
        return self.error

    def represent(self):
        angle, counter = 360.0 / len(self), len(self) - 1
        lenght = log((len(self)+1))*2
        output = ""
        for vertex in self._remove_vertex(self.error):
            output += vertex.represent(
                position="{angle}:{lenght}".format(
                    angle=angle*counter,
                    lenght=lenght)
            )
            counter -= 1
        output += "\\path[->]\n"
        for edge in self.edges:
            output += edge.represent()
        output += ";\n"
        return output

    def transition_by_letter(self, current_vertex, letter):
        if len(letter) != 1:
            raise ValueError("The letter argument must be a character.")

        if letter not in self.alphabet or current_vertex.error:
            return self.error

        for edge in self.edges:
            if edge.start == current_vertex and edge.letter == letter:
                return edge.end

        return self.error

    def accepts_word(self, word):
        current_vertex = self.fetch(initial)
        for letter in word:
            current_vertex = self.transition_by_letter(
                current_vertex, letter)
        if current_vertex.error:
            return False
        return current_vertex.final

    def clean_up(self):
        for edge in self.edges.copy():
            if edge.start.error or edge.end.error:
                self.edges.remove(edge)

    def multiply_automaton(self, other, operator):
        if self.alphabet != other.alphabet:
            raise ValueError("Alphabets must match!")
        vertices, edges = set(), set()
        error_pat_right, error_pat_left = compile("\dError"), compile("Error\d")
        for vertex_1 in self._remove_vertex(self.error):
            for vertex_2 in other._remove_vertex(self.error):
                for letter in self.alphabet:
                    new_vertex_1 = operator(vertex_1, vertex_2)
                    new_vertex_2 = operator(self.transition_by_letter(
                        vertex_1, letter),
                        other.transition_by_letter(vertex_2, letter))

                    # In cases of union the transition should behave like this.
                    if operator(False, True):
                        if search(error_pat_left, new_vertex_2.name):
                            new_vertex_2 = operator(
                                vertex_1,
                                other.transition_by_letter(vertex_2, letter))

                        if search(error_pat_right, new_vertex_2.name):
                            new_vertex_2 = operator(
                                self.transition_by_letter(vertex_1, letter),
                                vertex_2)

                    new_edge = Edge(new_vertex_1, new_vertex_2, letter)
                    edges.add(new_edge)
                    vertices.add(new_vertex_1)
                    vertices.add(new_vertex_2)
        return Automaton(vertices, edges, self.alphabet)

    def __and__(self, other):
        return self.multiply_automaton(other, operator.__and__)

    def __or__(self, other):
        return self.multiply_automaton(other, operator.__or__)

    # TODO: add subtraction to product.
    def __sub__(self, other):
        pass

    def __len__(self):
        return len(self.vertices) - 1
