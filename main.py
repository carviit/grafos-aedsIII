from graph import Graph

g = Graph()

g.add_node(0)
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)

g.add_edge(0, 3)
g.add_edge(0, 1)
g.add_edge(0, 5)

g.add_edge(1, 0)
g.add_edge(1, 3)
g.add_edge(1, 2)

g.add_edge(2, 3)
g.add_edge(2, 1)
g.add_edge(2, 4)

g.add_edge(3, 0)
g.add_edge(3, 1)
g.add_edge(3, 2)
g.add_edge(3, 3)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(3, 6)

g.add_edge(4, 2)
g.add_edge(4, 6)
g.add_edge(4, 3)

g.add_edge(5, 3)
g.add_edge(5, 0)
g.add_edge(5, 6)

g.add_edge(6, 3)
g.add_edge(6, 5)
g.add_edge(6, 4)

print(g)

print(g.is_valid_walk([0,3,0,5,3,4]))