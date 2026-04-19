class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj_list = {}

        for node in range(n):
            adj_list[node] = []

        for sourceNode, destNode, weight in edges:
            adj_list[sourceNode].append([destNode, weight])

        minHeap = [[0, src]]
        shortest = {}

        while minHeap:
            currWeight, currNode = heapq.heappop(minHeap)

            # Shortest path already found (we are using a minHeap so we will always have the min)
            if currNode in shortest:
                continue
            
            shortest[currNode] = currWeight

            for neighbor in adj_list[currNode]:
                neighborNode, neighborWeight = neighbor
                heapq.heappush(minHeap, [currWeight + neighborWeight, neighborNode])
        
        # Now mark any non-visited nodes as -1 (as specified in the description)
        for node in range(n):
            if node not in shortest:
                shortest[node] = -1
        
        return shortest
