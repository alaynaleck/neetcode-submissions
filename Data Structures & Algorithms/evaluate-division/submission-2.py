class UnionFind:
    def __init__(self):
        self.parents = {}
        self.weights = {}
    
    def add(self, vertex):
        if vertex not in self.parents:
            self.parents[vertex] = vertex
            self.weights[vertex] = 1
    
    def find(self, vertex):
        if vertex != self.parents[vertex]:
            parent = self.parents[vertex]
            self.parents[vertex] = self.find(self.parents[vertex])
            self.weights[vertex] *= self.weights[parent]
        return self.parents[vertex]

    def union(self, a, b, value):
        self.add(a)
        self.add(b)
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.parents[rootA] = rootB
            self.weights[rootA] = value * self.weights[b] / self.weights[a]

    def getRatio(self, a, b):
        if a not in self.parents or b not in self.parents or self.find(a) != self.find(b):
            return -1.0
        return self.weights[a] / self.weights[b]

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        uf = UnionFind()

        for i in range(len(equations)):
            a, b = equations[i]
            value = values[i]
            uf.union(a, b, value)

        return [uf.getRatio(a, b) for a, b in queries]
            



