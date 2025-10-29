# Implementation of prims and kruskals algorithm for MST using adujesent list

vertices = int(input("Enter the number of vertices: "))
edges_count = int(input("Enter the number of edges: "))

edges = []
for i in range(edges_count):
    S = input("Enter the Source: ")
    D = input("Enter the Destination: ")
    W = int(input("Enter the Weight: "))
    edges.append((S, D, W))

graph = {}
for i in range(vertices):
    graph[chr(ord('A') + i)] = []

for (s, d, w) in edges:
    graph[s].append((d, w))
    graph[d].append((s, w))

# Prim's Algorithm
def prim(graph, start):
    visited = set()
    mst_edges = []
    mst_weight = 0

    key = {v: float('inf') for v in graph}
    parent = {v: None for v in graph}
    key[start] = 0

    for _ in range(len(graph)):
        u = None
        min_key = float('inf')
        for vertex in graph:
            if vertex not in visited and key[vertex] < min_key:
                min_key = key[vertex]
                u = vertex

        if u is None:
            break

        visited.add(u)
        mst_weight += min_key

        if parent[u] is not None:
            mst_edges.append((parent[u], u, min_key))

        for v, w in graph[u]:
            if v not in visited and w < key[v]:
                key[v] = w
                parent[v] = u

    return mst_weight, mst_edges

# Kruskal's Algorithm 
class UnionFind:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for v in vertices:
            self.parent[v] = v
            self.rank[v] = 0

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            elif self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1
            return True
        return False

def kruskal(vertices, edges):
    uf = UnionFind(vertices)
    mst_weight = 0
    mst_edges = []

    edges_sorted = sorted(edges, key=lambda x: x[2])

    for u, v, w in edges_sorted:
        if uf.union(u, v):
            mst_weight += w
            mst_edges.append((u, v, w))

    return mst_weight, mst_edges

start_vertex = chr(ord('A'))

print("\nPrim's MST:")
prim_weight, prim_mst = prim(graph, start_vertex)
print(f"Total Weight: {prim_weight}")
print("Edges in MST:")
for u, v, w in prim_mst:
    print(f"{u} - {v} : {w}")

print("\nKruskal's MST:")
vertices_list = list(graph.keys())
kruskal_weight, kruskal_mst = kruskal(vertices_list, edges)
print(f"Total Weight: {kruskal_weight}")
print("Edges in MST:")
for u, v, w in kruskal_mst:
    print(f"{u} - {v} : {w}")
