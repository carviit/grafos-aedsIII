from graph import Graph

g = Graph()

g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)

g.add_edge(1, 2)

g.add_edge(2, 1)
g.add_edge(2, 3)

g.add_edge(3, 2)
g.add_edge(3, 4)

g.add_edge(4, 3)

print(g)




