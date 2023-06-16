from graph import Graph

g = Graph()

g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)

g.add_edge(1, 1)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)

g.add_edge(2, 1)
g.add_edge(2, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)

g.add_edge(3, 1)
g.add_edge(3, 2)
g.add_edge(3, 3)
g.add_edge(3, 4)

g.add_edge(4, 1)
g.add_edge(4, 2)
g.add_edge(4, 3)
g.add_edge(4, 4)

print(g)