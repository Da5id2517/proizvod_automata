from Edge import Edge
from Vertex import Vertex
from Automat import Automaton

"""Testing example.
"""

cvor0 = Vertex("0", True)
cvor1 = Vertex("1", False, True)
cvor2 = Vertex("2", True)
cvor3 = Vertex("3", False, True)

e1 = Edge(cvor0, cvor0, "a")
e2 = Edge(cvor0, cvor1, "b")
e3 = Edge(cvor2, cvor2, "b")
e4 = Edge(cvor2, cvor3, "a")

prvi = Automaton({cvor0, cvor1}, {e1, e2}, "ab")
drugi = Automaton({cvor3, cvor2}, {e3, e4}, "ab")
proizvod = prvi | drugi
print(proizvod.accepts_word("abbbb"))
for edge in proizvod.edges:
    print(edge)
print("--------------------------------")
