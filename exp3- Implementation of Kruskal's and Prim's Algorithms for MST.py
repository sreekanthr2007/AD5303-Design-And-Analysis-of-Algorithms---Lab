import heapq

# ---------- Union-Find for Kruskal ----------
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        return True


# ---------- Kruskal's Algorithm ----------
def kruskal(n, edges):
    edges.sort()  # Sort by weight

    uf = UnionFind(n)
    mst = []
    cost = 0

    for w, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            cost += w

            if len(mst) == n - 1:
                break

    return mst, cost


# ---------- Prim's Algorithm ----------
def prim(n, adj, start=0):
    INF = float('inf')

    key = [INF] * n
    parent = [-1] * n
    inMST = [False] * n

    key[start] = 0

    pq = [(0, start)]

    mst = []
    cost = 0

    while pq:
        w, u = heapq.heappop(pq)

        if inMST[u]:
            continue

        inMST[u] = True

        if parent[u] != -1:
            mst.append((parent[u], u, w))
            cost += w

        for v, wt in adj.get(u, []):
            if not inMST[v] and wt < key[v]:
                key[v] = wt
                parent[v] = u
                heapq.heappush(pq, (wt, v))

    return mst, cost


# ---------- Main Program ----------

n = 4

edges = [
    (10, 0, 1),
    (6, 0, 2),
    (5, 0, 3),
    (15, 1, 3),
    (4, 2, 3)
]

adj = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}

# Kruskal
mst1, cost1 = kruskal(n, edges)

print("Kruskal's MST:")
for u, v, w in mst1:
    print(f"{u} -- {v} : {w}")

print("Total Cost =", cost1)

print()

# Prim
mst2, cost2 = prim(n, adj)

print("Prim's MST:")
for u, v, w in mst2:
    print(f"{u} -- {v} : {w}")

print("Total Cost =", cost2)