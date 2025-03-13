# Algorithm for finding maximum and minimum spanning trees (MST) in weighted graphs
# Ensuring no cycles, it finds min. total weight that connects all the nodes in the graph

class DisjointSet:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal_algorithm(graph):
    # Sort edges by weight
    edges = sorted(graph, key=lambda edge: edge[2])

    # Initialize DisjointSet
    nodes = set()
    for edge in edges:
        nodes.update([edge[0], edge[1]])

    ds = DisjointSet(nodes)

    # Add edges while avoiding cycles
    mst = []
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))

    return mst

