# class UnionFind:

#     # REFERENCE DFS APPROACH AS WELL BELOW (CAN USE EITHER HERE)

#     # Purpose: Cycle detection
#     def __init__(self, n):
#         self.components = n
#         self.parents = [i for i in range(n)] # Path compression - update nodes along the path to point directly to the root, which "flattens" the tree for faster future lookups
#         self.rank = [1] * n # ranking -  keeping tree depth minimal
    
#     def find(self, node):
#         if node != self.parents[node]:
#             self.parents[node] = self.find(self.parents[node])

#         return self.parents[node]
    
#     def union(self, nodeU, nodeV):
#         unionU = self.find(nodeU)
#         unionV = self.find(nodeV)

#         # Share the same parents
#         if unionU == unionV:
#             return False

#         if self.rank[unionU] > self.rank[unionV]:
#             self.rank[unionU] += self.rank[unionV]
#             self.parents[unionV] = unionU
#         else:
#             self.rank[unionV] += self.rank[unionU]
#             self.parents[unionU] = unionV      

#         self.components -= 1
#         return True

#     def getComponents(self):
#         return self.components   

# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         unionF = UnionFind(n)

#         for nodeU, nodeV in edges:
#             if not unionF.union(nodeU, nodeV):
#                 return False

#         return unionF.getComponents() == 1

class Solution:
    def __init__(self):
        self.visited = set()
        self.adj_list = {}

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        for node in range(n):
            self.adj_list[node] = []
        
        for u, v in edges:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        
        self.dfs(0)
        
        return len(self.visited) == n
    
    def dfs(self, currNode):
        if currNode in self.visited:
            return

        self.visited.add(currNode)

        for neighborNode in self.adj_list[currNode]:
            self.dfs(neighborNode)
  
"""
Question:
1. What determines a valid tree? Is it every node in the tree being visited? YES
"""
