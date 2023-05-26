from graph import Graph

g = Graph()

g.add_node("A")
g.add_node("B")
g.add_node("C")

g.add_edge("A", "B")
g.add_edge("A", "C")

g.add_edge("B", "A")
g.add_edge("B", "C")

g.add_edge("C", "B")
g.add_edge("C", "A")



print(g)

print(g.is_directed())

print(g.is_regular())