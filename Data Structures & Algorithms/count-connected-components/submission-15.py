"""
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
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        adj_list = {
            0: [1], 
            1: [0, 2], 
            2: [1], 
            3: [4], 
            4: [3]
        }
        """
        adj_list = {}

        for course in range(n):
            adj_list[course] = []
        
        for nodeU, nodeV in edges:
            adj_list[nodeU].append(nodeV)
            adj_list[nodeV].append(nodeU)
        
        visited = set()
        components = 0

        # Visit each node
        for node in range(n):
            # Already visited and apart of a component dont revisit a course
            if node not in visited:
                self.dfs(adj_list, visited, node)
                components += 1  # increment for each connected component
                
        return components

    def dfs(self, adj_list, visited, node):
        visited.add(node)
         # Already visited and apart of a component dont revisit a course
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                self.dfs(adj_list, visited, neighbor)
"""
How DFS approach works:
n = 5, edges = [[0,1],[1,2],[3,4]]

before we iterate  - for course in range(n)
adj_list = {
    0: [1], 
    1: [0, 2], 
    2: [1], 
    3: [4], 
    4: [3]
}
visited = set()

When we first go though - for course in range(n) - visited is empty and we start with course = 0
    - the DFS call will go through adj_list to 0--1--2 creating ONE long component (also marking visited)
    - That way when we go to course = 1 and course = 2 in the for loop, they are already visited 
        and accounted for so we skip. 
    
"""


