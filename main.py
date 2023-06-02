from graph import Graph

g = Graph()

g.add_node(0)
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)

g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(0, 4)

g.add_edge(1, 0)
g.add_edge(1, 2)

g.add_edge(3, 0)

g.add_edge(4, 0)

print(g)

print(g.breadth_first_search(0))
