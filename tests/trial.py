from Edge import Edge
from Vertex import Vertex
from Automat import Automaton
from helpers import represent_automata

"""Testing example.
"""

cvor0 = Vertex("0", True)
cvor1 = Vertex("1", False, True)
cvor2 = Vertex("2", True)
cvor3 = Vertex("3", False, True)
print(cvor0.represent())

e1 = Edge(cvor0, cvor0, "b")
e2 = Edge(cvor0, cvor1, "a")
e3 = Edge(cvor2, cvor2, "a")
e4 = Edge(cvor2, cvor3, "b")

prvi = Automaton({cvor0, cvor1}, {e1, e2}, "ab")
print(represent_automata(prvi))
drugi = Automaton({cvor3, cvor2}, {e3, e4}, "ab")
print(represent_automata(drugi))
proizvod = prvi | drugi
print(proizvod.accepts_word("ab"))
print(represent_automata(proizvod))
print(represent_automata(proizvod|proizvod))
