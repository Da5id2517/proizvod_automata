from Edge import Edge
from Vertex import Vertex
from Automat import Automaton

"""Testing example.
"""

cvor0 = Vertex(0, True)
cvor1 = Vertex(1, False, True)
cvor2 = Vertex(2, True)
cvor3 = Vertex(3, False, True)

e1 = Edge(cvor0, cvor0, "a")
e2 = Edge(cvor0, cvor1, "b")
e3 = Edge(cvor2, cvor3, "a")
e4 = Edge(cvor3, cvor3, "b")

prvi = Automaton([cvor0, cvor1], [e1, e2], list("ab"))
drugi = Automaton([cvor2, cvor3], [e3, e4], list("ab"))
