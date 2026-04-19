class UnionFind:
    def __init__(self, n):
        self.components = n
        self.parents = [node for node in range(n)]
        self.rank = [1] * n
    
    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        
        return self.parents[node]
    
    def union(self, nodeU, nodeV):
        uNode = self.find(nodeU)
        vNode = self.find(nodeV)

        if uNode == vNode:
            return 
        
        if self.rank[uNode] < self.rank[vNode]:
            self.rank[vNode] += self.rank[uNode]
            self.parents[uNode] = vNode
        else:
            self.rank[uNode] += self.rank[vNode]
            self.parents[vNode] = uNode
        
        # Reduces one component
        self.components -= 1
    
    def getComponents(self):
        return self.components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFind = UnionFind(n)

        for nodeU, nodeV in edges:
            unionFind.union(nodeU, nodeV)
        
        return unionFind.getComponents()