class Graph:
    def __init__(self):
        self.graph = {}

    def hinzufuegen_kante(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def dfs(self, start):
        besucht = set()
        self.dfs_rek(start, besucht)

    def dfs_rek(self, scheitel, besucht):
        besucht.add(scheitel)
        print(scheitel, end=" ")

        if scheitel in self.graph:
            for nachbar in self.graph[scheitel]:
                if nachbar not in besucht:
                    self.dfs_rek(nachbar, besucht)

# Beispielgraph
#   1 - 2
#   |   |
#   3 - 4 - 5

# Erstellen des Beispielgraphs
graph = Graph()
graph.hinzufuegen_kante(1, 2)
graph.hinzufuegen_kante(1, 3)
graph.hinzufuegen_kante(3, 4)
graph.hinzufuegen_kante(4, 2)
graph.hinzufuegen_kante(4, 5)

# Tiefensuche (Depth-First Search) im Graphen
print("Tiefensuche:")
graph.dfs(1)
