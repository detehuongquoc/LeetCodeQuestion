
from typing import List
# [[0 for x in range(w)] for y in range(h)]
# [[] for y in rra]

# sử dụng UnionFind để connect tất cả các groop
# sau đó tách ra các group
# rồi sắp sếp các group lai với nhau, có thể dùng mảng để khi sắp xếp thì đã theo thứ tự
# để ý là index 1 sẽ bé hơn index 2


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
        if self.count == 1:
            return True
        else:
            return False

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        unionFind = UnionFind(len(s))
        for u, v in pairs:
            unionFind.union(u, v)

        group = unionFind.count
        if group == 1:
            return sorted(s)
        mp = {}
        for n in range(len(s)):
            mp.setdefault(unionFind.find(n), []).append(n)
        for v in mp.values():
            vals = [s[key] for key in v]
            
            for key, value in zip(v, sorted(vals)):
                print(key, value)
                s[key] = value
        return "".join(s)


solution = Solution()
print(solution.smallestStringWithSwaps("dcab",  [[0, 3], [1, 2]]))
