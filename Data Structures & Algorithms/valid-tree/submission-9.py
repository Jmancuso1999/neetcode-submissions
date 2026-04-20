class UnionFind:

    # REFERENCE DFS APPROACH AS WELL BELOW (CAN USE EITHER HERE)

    # Purpose: Cycle detection
    def __init__(self, n):
        self.components = n
        self.parents = [i for i in range(n)] # Path compression - update nodes along the path to point directly to the root, which "flattens" the tree for faster future lookups
        self.rank = [1] * n # ranking -  keeping tree depth minimal
    
    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])

        return self.parents[node]
    
    def union(self, nodeU, nodeV):
        unionU = self.find(nodeU)
        unionV = self.find(nodeV)

        # Share the same parents
        if unionU == unionV:
            return False

        if self.rank[unionU] > self.rank[unionV]:
            self.rank[unionU] += self.rank[unionV]
            self.parents[unionV] = unionU
        else:
            self.rank[unionV] += self.rank[unionU]
            self.parents[unionU] = unionV      

        self.components -= 1
        return True

    def getComponents(self):
        return self.components   

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # unionF = UnionFind(n)

        # for nodeU, nodeV in edges:
        #     if not unionF.union(nodeU, nodeV):
        #         return False

        # return unionF.getComponents() == 1

        # DFS Approach Time: O(V + E), Space: O(V + E)

        if len(edges) != n - 1: # More edges then nodes here
            return False
        
        adj_list = [[] for _ in range(n)]

        for nodeU, nodeV in edges:
            adj_list[nodeU].append(nodeV)
            adj_list[nodeV].append(nodeU)

        print(adj_list)
        visitedNodes = set()

        def dfs(node):
            if node in visitedNodes:
                return
            
            visitedNodes.add(node)

            for neighbor in adj_list[node]:
                dfs(neighbor)
        
        dfs(0)
        return len(visitedNodes) == n
