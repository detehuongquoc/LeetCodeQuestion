from collections import defaultdict
import heapq
from typing import List
# Kruskal's algorithm in Python

# sử dụng kruskal algortim để xác định cây khung ngắn nhất


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.count = 0

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Search function

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            self.count += weight
            print("%d - %d: %d" % (u, v, weight))


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = Graph(len(points))
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                print(i, j)
                u1, v1 = points[i]
                u2, v2 = points[j]
                graph.add_edge(i, j,
                               abs(u2 - u1) + abs(v2 - v1))

        print(graph.kruskal_algo())
        return graph.count


solution = Solution()
print(solution.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
