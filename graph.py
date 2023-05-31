class Graph:
    
    def __init__(self) -> None:
        self.adj_list = {}
        self.node_count = 0
        self.edge_count = 0

    def add_node(self, node):
        if node in self.adj_list:
            print(f"WARN: Node {node} already exists")
            return
        self.adj_list[node] = []
        self.node_count += 1

    def add_edge(self, node1, node2):
        try:
            self.adj_list[node1].append(node2)
            self.edge_count += 1
        except KeyError as e:
            print(f"WARN: Node {e} does not exist")

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def add_two_way_edge(self, node1, node2):
        self.add_edge(node1, node2)
        self.add_edge(node2, node1)

    def remove_node(self, node):
        for node2 in self.adj_list:
            if node in self.adj_list[node2]:
                self.adj_list[node2].remove(node)
                self.edge_count -= 1
        self.edge_count -= len(self.adj_list[node])
        self.node_count -= 1
        self.adj_list.pop(node)

    def remove_edge(self, node1, node2):
        try:
          self.adj_list[node1].remove(node2)
          self.edge_count -= 1
        except KeyError as e:
            print(f"WARN: Node {e} does not exist")
        except ValueError as e:
            print(f"WARN: Edge {node1} -> {node2} does not exist")

    def degree_out(self, node):
        return len(self.adj_list[node])
    
    def degree_in(self, node):
        count = 0
        for node2 in self.adj_list:
            if node in self.adj_list[node2]:
                count += 1
        return count
    
    def highest_degree_out(self):
        highest = float("-inf")
        for node in self.adj_list:
            if self.degree_out(node) > highest:
                highest = self.degree_out(node)
        return highest

    def highest_degree_in(self):
        highest = float("-inf")
        for node in self.adj_list:
            if self.degree_in(node) > highest:
                highest = self.degree_in(node)
        return highest

    def density(self):
        return self.edge_count / (self.node_count * (self.node_count - 1))

    def is_complete(self):
        return self.density() == 1

    def __str__(self) -> str:
        output = "Nodes: " + str(self.node_count) + "\n"
        output += "Edges: " + str(self.edge_count) + "\n"
        output += str(self.adj_list)
        return output
    
    def there_is_edge(self, node1, node2):
        return node2 in self.adj_list[node1]
    
    def is_directed(self):
        for node1 in self.adj_list:
            for node2 in self.adj_list[node1]:
                if not self.there_is_edge(node2, node1):
                    return True
        return False
    
    def neighbors(self, node):
        return self.adj_list[node]
    
    def is_regular(self):
        degree_frist_node = self.degree_out(list(self.adj_list)[0])
        for node in self.adj_list:
            if self.degree_out(node) != degree_frist_node:
                return False
        return True
    
    def complement(self):
        g2 = Graph()
        for node in self.adj_list:
            g2.add_node(node)
            for node2 in self.adj_list:
                if node != node2 and not self.there_is_edge(node, node2):
                    g2.add_edge(node,node2)
        return g2
    
    def is_subgraph_of(self, g2):
        for node in self.adj_list:
            if node in self.adj_list:
                return False
        for node2 in self.adj_list:
            if node2 not in g2.adj_list[node]:
                return False
        return True
    
    def is_connected(self):
        pass