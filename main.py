from graph import Graph
from weightedGraph import WeightedGraph

# Aula 8 - Grafos ponderados
g = WeightedGraph()
g.read_file("USA-road.txt")
print(g.bellman_ford_improved("0"))
print(g)