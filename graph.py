class Graph:
    def __init__(self) -> None:
        self.adj_list = {}
        self.node_count = 0
        self.edge_count = 0

    # Adiciona vértice (nó)
    def add_node(self, node):
        if node in self.adj_list:
            print(f"WARN: Node {node} already exists")
            return
        self.adj_list[node] = []
        self.node_count += 1

    # Adiciona aresta
    def add_edge(self, node1, node2):
        try:
            self.adj_list[node1].append(node2)
            self.edge_count += 1
        except KeyError as e:
            print(f"WARN: Node {e} does not exist")

    # Adiciona nós a partir de uma lista
    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    # Adiciona aresta ida e volta entre nós
    def add_two_way_edge(self, node1, node2):
        self.add_edge(node1, node2)
        self.add_edge(node2, node1)

    # Remove nó
    def remove_node(self, node):
        for node2 in self.adj_list:
            if node in self.adj_list[node2]:
                self.adj_list[node2].remove(node)
                self.edge_count -= 1
        self.edge_count -= len(self.adj_list[node])
        self.node_count -= 1
        self.adj_list.pop(node)

    # Remove aresta
    def remove_edge(self, node1, node2):
        try:
            self.adj_list[node1].remove(node2)
            self.edge_count -= 1
        except KeyError as e:
            print(f"WARN: Node {e} does not exist")
        except ValueError as e:
            print(f"WARN: Edge {node1} -> {node2} does not exist")

    # Retorna o número de arestas que saem de um nó
    def degree_out(self, node):
        return len(self.adj_list[node])

    # Retorna o número de arestas que entram em um nó
    def degree_in(self, node):
        count = 0
        for node2 in self.adj_list:
            if node in self.adj_list[node2]:
                count += 1
        return count

    # Retorna o maior grau de saída de todos os nós em um grafo
    def highest_degree_out(self):
        highest = float("-inf")
        for node in self.adj_list:
            if self.degree_out(node) > highest:
                highest = self.degree_out(node)
        return highest

    # Retorna o maior grau de entrada de todos os nós em um grafo
    def highest_degree_in(self):
        highest = float("-inf")
        for node in self.adj_list:
            if self.degree_in(node) > highest:
                highest = self.degree_in(node)
        return highest

    # Retorna a densidade do grafo entre [0-1]
    def density(self):
        return self.edge_count / (self.node_count * (self.node_count - 1))

    # Verifica se o grafo é completo
    def is_complete(self):
        return self.density() == 1

    # Verifica a existencia de aresta entre 2 nós
    def there_is_edge(self, node1, node2):
        return node2 in self.adj_list[node1]

    # Verifica se o grafo é direcionado
    def is_directed(self):
        for node1 in self.adj_list:
            for node2 in self.adj_list[node1]:
                if not self.there_is_edge(node2, node1):
                    return True
        return False

    # Informa os vizinhos (ligações) de um nó,
    def neighbors(self, node):
        return self.adj_list[node]

    # Verifica se o grafo é regular
    def is_regular(self):
        degree_frist_node = self.degree_out(list(self.adj_list)[0])
        for node in self.adj_list:
            if self.degree_out(node) != degree_frist_node:
                return False
        return True

    # Retorna o complemento de um grafo (grafo com número de ligações que faltam para ser completo)
    def complement(self):
        g2 = Graph()
        for node in self.adj_list:
            g2.add_node(node)
            for node2 in self.adj_list:
                if node != node2 and not self.there_is_edge(node, node2):
                    g2.add_edge(node, node2)
        return g2
    
    # Verifica se o grafo passado como parâmetro é sub-grafo do grafo original
    def is_subgraph_of(self, g2):       
        for node in g2.adj_list:
            if node not in self.adj_list:
                return False
            for neighbor in g2.adj_list[node]:
                if neighbor not in self.adj_list[node]:
                    return False
        return True

    # Verifica se o grafo é conexo (conectado)
    def is_connected(self):
        return len(self.dfs(list(self.adj_list)[0])) == self.node_count

    # Verifica se a lista de nós possui aresta entre um nó e o proximo da lista
    def is_valid_walk(self, walk):
        for i in range(len(walk) - 1):
            if not self.there_is_edge(walk[i], walk[i + 1]):
                return False

        return True

    def is_valid_trail(self, trail):
        # Pode ser mais rápido usando dicionário
        used_edges = []
        for i in range(len(trail) - 1):
            if not self.there_is_edge(trail[i], trail[i + 1]):
                return False
            edge = (trail[i], trail[i + 1])
            if edge in used_edges:
                return False
            used_edges.append(edge)
        return True

    def is_valid_circuit(self, circuit):
        if self.is_valid_trail(circuit):
            return circuit[0] == circuit[-1]

    def is_valid_path(self, path):
        # Pode ser mais rápido usando dicionário
        used_nodes = []
        used_edges = []
        for i in range(len(path) - 1):
            if not self.there_is_edge(path[i], path[i + 1]):
                return False
            edge = (path[i], path[i + 1])
            if edge in used_edges:
                return False
            used_edges.append(edge)
            node = path[i]
            if node in used_nodes:
                return False
            used_nodes.append(node)
        return True

    def is_valid_cycle(self, cycle):
        if self.is_valid_path(cycle):
            return cycle[0] == cycle[-1]

    # Busca em largura em um grafo dado um nó de origem
    def breadth_first_search(self, sourceNode):
        desc = []

        for node in self.adj_list:
            desc.append(node)
            desc[node] = 0

        q = []  # Fila de nós a processar
        r = []  # Resposta - Ordem de descoberta
        desc[sourceNode] = 1

        while len(q) > 0:
            u = q.pop(0)

        for node in self.adj_list[u]:
            if desc[node] == 0:
                desc[node] = 1
                q.append(node)
                r.append(node)

        return r

    def dfs_rec_visit(self, u, desc, R):
        desc[u] = 1
        R.append(u)
        for v in self.adj_list[u]:
            if desc[v] == 0:
                self.dfs_rec_visit(v, desc, R)

    def dfs_rec(self, s):
        desc = {}
        for node in self.adj_list:
            desc[node] = 0
        R = []
        self.dfs_rec_visit(s, desc, R)
        return R

    def dfs(self, s):
        desc = {}
        for node in self.adj_list:
            desc[node] = 0
        S = [s]
        R = [s]
        desc[s] = 1
        while len(S) > 0:
            u = S[-1]
            unstack = True
            for v in self.adj_list[u]:
                if desc[v] == 0:
                    desc[v] = 1
                    S.append(v)
                    R.append(v)
                    unstack = False
                    break
            if unstack:
                S.pop()
        return R

    def __str__(self) -> str:
        output = "Nodes: " + str(self.node_count) + "\n"
        output += "Edges: " + str(self.edge_count) + "\n"
        output += str(self.adj_list)
        return output
