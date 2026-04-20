class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj_list = {}

        for node in range(n):
            adj_list[node] = []
        
        for nodeU, nodeV, weight in edges:
            adj_list[nodeU].append([nodeV, weight])
        
        minHeap = [[0, src]]

        shortest = {}

        while minHeap:
            currWeight, currNode = heapq.heappop(minHeap)

            if currNode in shortest:
                continue
            
            shortest[currNode] = currWeight

            for neighborNode, neighborWeight in adj_list[currNode]:
                heapq.heappush(minHeap, [currWeight + neighborWeight, neighborNode])

        for node in range(n):
            if node not in shortest:
                shortest[node] = -1
        
        return shortest