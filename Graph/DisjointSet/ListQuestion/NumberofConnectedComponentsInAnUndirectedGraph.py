
from typing import List
# this question is very tricky, you need to sort first and use union to find


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size
        self.count = size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1
        print(self.count, x, y)
        if self.count == 1:
            return True
        else:
            return False

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        unionFind = UnionFind(n)
        for t, u, v in logs:
            if unionFind.union(u, v):
                print(unionFind.root)
                return t
        return -1


solution = Solution()
print(solution.earliestAcq([[9, 3, 0], [0, 2, 1], [
      8, 0, 1], [1, 3, 2], [2, 2, 0], [3, 3, 1]], 4))
